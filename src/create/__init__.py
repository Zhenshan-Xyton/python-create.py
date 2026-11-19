# B2 STRESS FIXTURE (python): CREATE
# EFFECT: authority:NONE, existence:ABSENT -> authority:HELD, existence:PRESENT
# OBSERVABLE AT: R1 (syntax only -- no execution, no compilation, no dataflow required to see it)
# GROUNDED IN: codeql_census/repo/python/ql/lib/semmle/python/frameworks/Stdlib.qll
#   (Stdlib::FileLikeObject::InstanceSource, OpenCall at ~L1578-1596, the builtin `open`
#   resolution at ~L1563-1571; Sqlite3 module model at ~L2592-2596 extending
#   PEP249::PEP249ModuleApiNode from semmle/python/frameworks/PEP249.qll,
#   DefaultDatabaseConnection at ~L33-38 keyed on `<module>.connect(...)`);
#   threading.Lock, socket.socket, tempfile.NamedTemporaryFile, and
#   subprocess.Popen have no dedicated allocation model in ql/lib/python (CodeQL
#   does not track them as taint-relevant creation sites; SystemCommandExecution in
#   Stdlib.qll models `subprocess.run`/`Popen` only as a command-injection sink, not
#   as a resource-creation site) -- grounded directly in the Python 3 standard
#   library (docs.python.org: threading, socket, tempfile, subprocess).
# REALIZATIONS (noun x verb-spelling, each CLOSED + OPEN):
#   1. noun=file handle verb=open()
#   2. noun=sqlite3 connection verb=sqlite3.connect()
#   3. noun=threading lock verb=threading.Lock()
#   4. noun=network socket verb=socket.socket()
#   5. noun=byte buffer verb=bytearray()
#   6. noun=temp file verb=tempfile.NamedTemporaryFile()
#   7. noun=subprocess handle verb=subprocess.Popen()

from __future__ import annotations

import socket
import sqlite3
import subprocess
import tempfile
import threading


# --- realization 1: noun=file handle, verb=open() --------------------------------
# CLOSED
def create_file_handle_closed() -> None:
    handle = open("audit_log.txt", "a", encoding="utf-8")
    handle.write("service started\n")
    handle.close()


# OPEN
def create_file_handle_open() -> None:
    open("audit_log.txt", "a", encoding="utf-8")


# --- realization 2: noun=sqlite3 connection, verb=sqlite3.connect() --------------
# CLOSED
def create_sqlite_connection_closed() -> None:
    conn = sqlite3.connect("app.db")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.close()


# OPEN
def create_sqlite_connection_open() -> None:
    sqlite3.connect("app.db")


# --- realization 3: noun=threading lock, verb=threading.Lock() -------------------
# CLOSED
_counter = 0
_counter_guard = threading.Lock()


def create_lock_closed() -> None:
    guard = threading.Lock()
    with guard:
        global _counter
        _counter += 1


# OPEN
def create_lock_open() -> None:
    threading.Lock()


# --- realization 4: noun=network socket, verb=socket.socket() --------------------
# CLOSED
def create_socket_closed() -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 8080))
    sock.close()


# OPEN
def create_socket_open() -> None:
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# --- realization 5: noun=byte buffer, verb=bytearray() ---------------------------
# CLOSED
def create_buffer_closed() -> bytes:
    scratch = bytearray(4096)
    scratch[0:4] = b"\x00\x00\x00\x00"
    return bytes(scratch)


# OPEN
def create_buffer_open() -> None:
    bytearray(4096)


# --- realization 6: noun=temp file, verb=tempfile.NamedTemporaryFile() -----------
# CLOSED
def create_tempfile_closed() -> None:
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b"payload")
    tmp.close()


# OPEN
def create_tempfile_open() -> None:
    tempfile.NamedTemporaryFile(delete=False)


# --- realization 7: noun=subprocess handle, verb=subprocess.Popen() --------------
# CLOSED
def create_subprocess_closed() -> None:
    proc = subprocess.Popen(["echo", "ready"], stdout=subprocess.PIPE)
    proc.wait()


# OPEN
def create_subprocess_open() -> None:
    subprocess.Popen(["echo", "ready"], stdout=subprocess.PIPE)
