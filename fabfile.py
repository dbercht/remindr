from fabric import local


def serve():
    local("python app.py")