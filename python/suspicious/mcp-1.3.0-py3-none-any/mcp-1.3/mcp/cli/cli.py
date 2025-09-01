def _get_npx_command():
    """Get the correct npx command for the current platform."""
    if sys.platform == "win32":
        # Try both npx.cmd and npx.exe on Windows
        for cmd in ["npx.cmd", "npx.exe", "npx"]:
            try:
                subprocess.run(
                    [cmd, "--version"], check=True, capture_output=True, shell=True
                )
                return cmd
            except subprocess.CalledProcessError:
                continue
        return None
    return "npx"  # On Unix-like systems, just use npx