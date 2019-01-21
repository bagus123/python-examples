import os
import click
import pyAesCrypt
import cx_Oracle

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
encryptPassword = "random_string"


@click.group()
def main():
    """
    Simple Oracle CLI
    """
    pass


# config -u "oracle-user" -p "pracle-password" -h "192.168.1.200" -sid "ORACLESID"
@main.command()
@click.option('--user', '-u', multiple=False, default='', help='User Oracle')
@click.option('--password', '-p', multiple=False, default='', help='Password Oracle')
@click.option('--host', '-h', multiple=False, default='', help='Host Oracle example 192.168.1.200, localhost')
@click.option('--port', '-port', multiple=False, default='1521', help='Port Oracle default 1521')
@click.option('--sid', '-sid', multiple=False, default='', help='SID Oracle')
def config(user, password, host, port, sid):
    click.echo('user {0}'.format(user))
    click.echo('password {0}'.format(password))
    file = open("connection.dat", "w")
    file.write(format(user)+"|"+format(password)+"|" +format(host)+"|"+format(port)+"|"+format(sid))
    file.close()
    pyAesCrypt.encryptFile("connection.dat", "connection.dat.aes", encryptPassword, bufferSize)
    if os.path.exists("connection.dat"):
        os.remove("connection.dat")


@main.command()
@click.argument('arg')
def query(arg):
    if os.path.exists("connection.dat.aes"):
        pyAesCrypt.decryptFile("connection.dat.aes", "connection_out.dat", encryptPassword, bufferSize)
        file = open("connection_out.dat", "r")
        strConfig = file.read()
        config = strConfig.split('|')
        file.close()
        if os.path.exists("connection_out.dat"):
            os.remove("connection_out.dat")
			
        oracle = {}
        oracle["user"] = config[0]
        oracle["password"] = config[1]
        oracle["host"] = config[2]
        oracle["port"] = config[3]
        oracle["sid"] = config[4]

        my_dsn = cx_Oracle.makedsn( oracle["host"],int(oracle["port"]),sid=oracle["sid"] )
        conn = cx_Oracle.connect(user=oracle["user"], password=oracle["password"] , dsn=my_dsn)
        cur = conn.cursor()
        cur.execute(format(arg))
        res = cur.fetchall()
        click.echo("%s"%res)
        cur.close()
        conn.close()

@main.command()
def version():
    click.echo("version 1.0")


if __name__ == '__main__':
    main()
