from fastapi import Response

__all__ = ('nginx_cache',)


def nginx_cache(timeout: int):
    def nginx_dependence(response: Response):
        response.headers['X-Accel-Expires'] = str(timeout)
        return response
    return nginx_dependence
