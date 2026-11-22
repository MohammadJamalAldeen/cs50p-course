from watch import parse


def test_https_www():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_http_www():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_https_no_www():
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_text_before_iframe():
    assert parse(
        'هاد هو الرابط <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == None
