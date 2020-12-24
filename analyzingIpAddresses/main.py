import glob


def analyzingIpAddresses(root):
    files = glob.glob("{}/**/*.*".format(root), recursive=True)
    # print(files)
    ret = ""
    with open(files[0]) as fp:
        content = fp.read()
        print(files[0])
        print(content)
    print(ret)
    return ret


if __name__ == "__main__":
    expect_result = """0.0.0.0
127.0.0.1
127.0.49.1
127.0.64.1
127.65.64.1
127.98.0.1
128.128.4.11
128.57.107.76
128.68.4.11
128.96.107.55
128.99.107.55
128.99.58.55
15.128.4.65
26.56.4.23
67.128.4.11
7.7.7.8
74.0.65.76
77.255.255.254"""

    print(expect_result)
    got = analyzingIpAddresses("./test1/files")

    if got != expect_result:
        print("Error! got:", got, ", expect:", expect_result)
