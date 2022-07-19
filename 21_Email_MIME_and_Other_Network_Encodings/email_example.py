import os, email


def unpack_mail(mail_file, dest_dir):
    ''' Given file object mail_file, open for reading, and dest_dir, a
        string that is a path to an existing, writable directory,
        unpack each part of the mail message from mail_file to a
        file within dest_dir.
    '''
    with mail_file:
        msg = email.message_from_file(mail_file)
    for part_number, part in enumerate(msg.walk()):
        if part.get_content_maintype() == 'multipart':
            # we get each specific part later in the loop,
            # so, nothing to do for the 'multipart' itself
            continue
        dest = part.get_filename()
        if dest is None:
            dest = part.get_param('name')
        if dest is None:
            dest = 'part-{}'.format(part_number)
        # In real life, make sure that dest is a reasonable filename
        # for your OS; otherwise, mangle that name until it is
        with open(os.path.join(dest_dir, dest), 'wb') as f:
            f.write(part.get_payload(decode=True))


def pack_mail(source_dir, **headers):
    ''' Given source_dir, a string that is a path to an existing,
        readable directory, and arbitrary header name/value pairs
        passed in as named arguments, packs all the files directly
        under source_dir (assumed to be plain text files) into a
        mail message returned as a MIME-formatted string.
    '''

    msg = email.message.Message()
    for name, value in headers.items():
        msg[name] = value
    msg['Content-type'] = 'multipart/mixed'
    filenames = next(os.walk(source_dir))[-1]
    for filename in filenames:
        m = email.message.Message()
        m.add_header('Content-type', 'text/plain', name=filename)
        with open(os.path.join(source_dir, filename), 'r') as f:
            m.set_payload(f.read())
        msg.attach(m)
    return msg.as_string()
