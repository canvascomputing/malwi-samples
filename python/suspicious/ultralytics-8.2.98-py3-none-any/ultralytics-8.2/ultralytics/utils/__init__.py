def is_online() -> bool:
    """
    Check internet connectivity by attempting to connect to a known online host.

    Returns:
        (bool): True if connection is successful, False otherwise.
    """
    with contextlib.suppress(Exception):
        assert str(os.getenv("YOLO_OFFLINE", "")).lower() != "true"  # check if ENV var YOLO_OFFLINE="True"
        import socket

        for dns in ("1.1.1.1", "8.8.8.8"):  # check Cloudflare and Google DNS
            socket.create_connection(address=(dns, 80), timeout=2.0).close()
            return True
    return False