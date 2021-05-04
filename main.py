from beautifultable import BeautifulTable


def init_table():
    table = BeautifulTable(maxwidth=200)
    table.columns.header = ['height', 'z', 'time']

    return table

def init_file():
    f = open('result.txt', 'w')
    f.write(f'height\theight (double step)\tz\ttime\n')

    return f


g = 9.8
rho0 = 1000
rho1 = 650
S = 314
d = 5
k = S / d
eta = 1
V = 300
H = -1000
alpha = 0.01

def f(z):
    return z

def G(h, z):
    return g * ((rho0 - rho1) / rho1) - ((k * eta) / (rho1 * V)) * (1 + alpha * (h / H)) * z


def submarine_surfacing(init_h, end_h, step):
    table = init_table()
    file = init_file()

    h = h2 = init_h
    z = 0.0
    t = 0.0


    file.write(f'{h}\t{h2}\t{z}\t{t}\n')
    table.rows.append([h, z, t])

    while h < end_h:
        k1 = f(z)
        m1 = G(h, z)
        k2 = f(z + m1 / 2)
        m2 = G(h + k1 / 2, z + m1 / 2)
        k3 = f(z + m2 / 2)
        m3 = G(h + k2 / 2, z + m2 / 2)
        k4 = f(z + m3)
        m4 = G(h + k3, z + m3)
        h += step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        h2 += 2 * step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        z += step * (m1 + 2 * m2 + 2 * m3 + m4) / 6
        t += 1

        file.write(f'{h}\t{h2}\t{z}\t{t}\n')
        table.rows.append([h, z, t])

    file.close()
    print(table)


if __name__ == '__main__':
    submarine_surfacing(init_h=-1000, end_h=0, step=1)