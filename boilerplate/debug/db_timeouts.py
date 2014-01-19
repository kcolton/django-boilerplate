import socket
import logging
import time

logger = logging.getLogger(__name__)


def get_nameservers():
    try:
        import DNS
    except ImportError:
        raise Exception('You must have the PyDNS package installed to fetch the nameserver config')

    nameservers = DNS.defaults.get('server', None)

    if not nameservers:
        logger.info('discovering nameservers ...')
        DNS.DiscoverNameServers()
        nameservers = DNS.defaults.get('server', None)

    logger.info('nameservers: %s' % nameservers)
    return nameservers


def resolve_hostname(hostname, timeout=2, nameservers=False):
    if nameservers:
        get_nameservers()

    old_default = socket.getdefaulttimeout()
    socket.setdefaulttimeout(timeout)

    start_time = time.time()
    logger.info('resolving hostname: "%s"' % hostname)
    try:
        res = socket.gethostbyname(hostname)
        duration = time.time() - start_time

        logger.info('lookup success: %s LOOKUPDURATION(%s)' % (res, duration))
    except socket.error as exc:
        logger.error('hostname lookup failed: %s' % exc)
    finally:
        socket.setdefaulttimeout(old_default)


def resolve_django_db_hostnames():
    from django.conf import settings

    for db in settings.DATABASES.values():
        if 'HOST' in db:
            resolve_hostname(db['HOST'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    resolve_hostname('www.google.com', nameservers=True)
    resolve_hostname('10.4.13.5')