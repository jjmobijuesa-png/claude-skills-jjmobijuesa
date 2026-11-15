"""IPP directo a la HP Smart Tank, sin pasar por la cola WSD de Windows.

Uso:
  python ipp_directo.py atributos [host]
  python ipp_directo.py imprimir archivo.pdf [host] [--formato application/pdf] [--copias 1]
  python ipp_directo.py trabajos [host]

host por defecto: HPC4225C (resuelve a la IP de la red local).
Probado el 13-nov-2026: la cola WSD aceptaba los trabajos y los perdía; IPP directo imprime.
"""
import socket, struct, sys, http.client

HOST = 'HPC4225C'
RUTAS = ['/ipp/print', '/ipp/printer', '/ipp']


def attr(tag, name, value):
    if isinstance(value, int) and tag in (0x21, 0x23):
        v = struct.pack('>i', value)
    elif isinstance(value, bool):
        v = bytes([1 if value else 0])
    else:
        v = value.encode('utf-8')
    n = name.encode('utf-8')
    return bytes([tag]) + struct.pack('>H', len(n)) + n + struct.pack('>H', len(v)) + v


def peticion(op, req_id, uri, extra_op=b'', extra_job=b''):
    b = struct.pack('>BBHI', 2, 0, op, req_id)
    b += b'\x01'
    b += attr(0x47, 'attributes-charset', 'utf-8')
    b += attr(0x48, 'attributes-natural-language', 'es')
    b += attr(0x45, 'printer-uri', uri)
    b += attr(0x42, 'requesting-user-name', 'claude')
    b += extra_op
    if extra_job:
        b += b'\x02' + extra_job
    b += b'\x03'
    return b


def parse(data):
    ver, status, rid = struct.unpack('>HHI', data[:8])
    i = 8; res = {}; grupo = None; ultimo = None
    while i < len(data):
        t = data[i]; i += 1
        if t < 0x10:
            if t == 3: break
            grupo = t; continue
        nl = struct.unpack('>H', data[i:i+2])[0]; i += 2
        name = data[i:i+nl].decode('utf-8', 'replace'); i += nl
        vl = struct.unpack('>H', data[i:i+2])[0]; i += 2
        raw = data[i:i+vl]; i += vl
        if t in (0x21, 0x23) and vl == 4:
            val = struct.unpack('>i', raw)[0]
        elif t == 0x22:
            val = bool(raw[0])
        else:
            val = raw.decode('utf-8', 'replace')
        if name:
            ultimo = name; res.setdefault((grupo, name), []).append(val)
        elif ultimo:
            res[(grupo, ultimo)].append(val)
    return status, res


def enviar(host, ruta, cuerpo):
    c = http.client.HTTPConnection(host, 631, timeout=60)
    c.request('POST', ruta, body=cuerpo, headers={'Content-Type': 'application/ipp'})
    r = c.getresponse(); d = r.read(); c.close()
    if r.status != 200:
        raise RuntimeError(f'HTTP {r.status} en {ruta}')
    return parse(d)


def ruta_valida(host):
    for ruta in RUTAS:
        uri = f'ipp://{host}:631{ruta}'
        try:
            st, res = enviar(host, ruta, peticion(0x000B, 1, uri))
            if st < 0x0100:
                return ruta, uri, res
        except Exception as e:
            print('  ruta', ruta, 'falló:', e)
    raise SystemExit('Ninguna ruta IPP respondió')


def main():
    a = sys.argv[1:]
    cmd = a[0]
    if cmd == 'imprimir':
        archivo = a[1]; resto = a[2:]
    else:
        archivo = None; resto = a[1:]
    host = next((x for x in resto if not x.startswith('--') and x not in ('application/pdf',)), HOST)
    formato = 'application/pdf'
    if '--formato' in resto: formato = resto[resto.index('--formato') + 1]
    copias = int(resto[resto.index('--copias') + 1]) if '--copias' in resto else 1
    ruta, uri, res = ruta_valida(host)
    if cmd == 'atributos':
        for k in ['printer-state', 'printer-state-reasons', 'printer-make-and-model', 'document-format-supported',
                  'media-default', 'media-ready', 'sides-supported', 'print-color-mode-supported', 'marker-levels', 'marker-names']:
            for (g, n), v in res.items():
                if n == k: print(f'{n}: {v}')
        print('ruta:', ruta)
    elif cmd == 'trabajos':
        st, r = enviar(host, ruta, peticion(0x000A, 3, uri, attr(0x44, 'which-jobs', 'not-completed')))
        print('estado', hex(st)); [print(n, v) for (g, n), v in r.items() if g == 2]
    elif cmd == 'imprimir':
        doc = open(archivo, 'rb').read()
        op = attr(0x42, 'job-name', archivo.split('\\')[-1].split('/')[-1][:60]) + attr(0x49, 'document-format', formato)
        job = attr(0x21, 'copies', copias) + attr(0x44, 'media', 'iso_a4_210x297mm') + attr(0x44, 'print-color-mode', 'color')
        st, r = enviar(host, ruta, peticion(0x0002, 2, uri, op, job) + doc)
        print('Print-Job estado', hex(st))
        for (g, n), v in r.items():
            if n in ('job-id', 'job-state', 'job-state-reasons', 'status-message'): print(' ', n, v)


if __name__ == '__main__':
    main()
