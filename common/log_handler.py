from logstash import TCPLogstashHandler
from logstash.formatter import LogstashFormatterVersion1, LogstashFormatterVersion0


class FormatterVersion1(LogstashFormatterVersion1):
    def format(self, record):
        # Create message dict
        message = {
            '@timestamp': self.format_timestamp(record.created),
            '@version': '1',
            'message': record.getMessage(),
            'host': self.host,
            'path': record.pathname,
            'tags': self.tags,
            'type': self.message_type,

            # Extra Fields
            'level': record.levelname,
            'lineno': record.lineno,
            'logger_name': record.name,
        }

        # Add extra fields
        message.update(self.get_extra_fields(record))

        # If exception, add debug info
        if record.exc_info:
            message.update(self.get_debug_fields(record))

        return self.serialize(message)


class ConsumeLogstashHandler(TCPLogstashHandler):

    def __init__(self, host, port=5959, message_type='logstash', tags=None, fqdn=False, version=0):
        super(TCPLogstashHandler, self).__init__(host, port)
        if version == 1:
            self.formatter = FormatterVersion1(message_type, tags, fqdn)
        else:
            self.formatter = LogstashFormatterVersion0(message_type, tags, fqdn)

    def makePickle(self, record):
        return self.formatter.format(record) + b'\n'
