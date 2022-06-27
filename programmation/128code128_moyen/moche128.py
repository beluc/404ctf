import socket
from PIL import Image
from io import BytesIO
import base64

CODE128_CHART = """
0       212222  space   space   00
1       222122  !       !       01
2       222221  "       "       02
3       121223  #       #       03
4       121322  $       $       04
5       131222  %       %       05
6       122213  &       &       06
7       122312  '       '       07
8       132212  (       (       08
9       221213  )       )       09
10      221312  *       *       10
11      231212  +       +       11
12      112232  ,       ,       12
13      122132  -       -       13
14      122231  .       .       14
15      113222  /       /       15
16      123122  0       0       16
17      123221  1       1       17
18      223211  2       2       18
19      221132  3       3       19
20      221231  4       4       20
21      213212  5       5       21
22      223112  6       6       22
23      312131  7       7       23
24      311222  8       8       24
25      321122  9       9       25
26      321221  :       :       26
27      312212  ;       ;       27
28      322112  <       <       28
29      322211  =       =       29
30      212123  >       >       30
31      212321  ?       ?       31
32      232121  @       @       32
33      111323  A       A       33
34      131123  B       B       34
35      131321  C       C       35
36      112313  D       D       36
37      132113  E       E       37
38      132311  F       F       38
39      211313  G       G       39
40      231113  H       H       40
41      231311  I       I       41
42      112133  J       J       42
43      112331  K       K       43
44      132131  L       L       44
45      113123  M       M       45
46      113321  N       N       46
47      133121  O       O       47
48      313121  P       P       48
49      211331  Q       Q       49
50      231131  R       R       50
51      213113  S       S       51
52      213311  T       T       52
53      213131  U       U       53
54      311123  V       V       54
55      311321  W       W       55
56      331121  X       X       56
57      312113  Y       Y       57
58      312311  Z       Z       58
59      332111  [       [       59
60      314111  \       \       60
61      221411  ]       ]       61
62      431111  ^       ^       62
63      111224  _       _       63
64      111422  NUL     `       64
65      121124  SOH     a       65
66      121421  STX     b       66
67      141122  ETX     c       67
68      141221  EOT     d       68
69      112214  ENQ     e       69
70      112412  ACK     f       70
71      122114  BEL     g       71
72      122411  BS      h       72
73      142112  HT      i       73
74      142211  LF      j       74
75      241211  VT      k       75
76      221114  FF      l       76
77      413111  CR      m       77
78      241112  SO      n       78
79      134111  SI      o       79
80      111242  DLE     p       80
81      121142  DC1     q       81
82      121241  DC2     r       82
83      114212  DC3     s       83
84      124112  DC4     t       84
85      124211  NAK     u       85
86      411212  SYN     v       86
87      421112  ETB     w       87
88      421211  CAN     x       88
89      212141  EM      y       89
90      214121  SUB     z       90
91      412121  ESC     {       91
92      111143  FS      |       92
93      111341  GS      }       93
94      131141  RS      ~       94
95      114113  US      DEL     95
96      114311  FNC3    FNC3    96
97      411113  FNC2    FNC2    97
98      411311  ShiftB  ShiftA  98
99      113141  CodeC   CodeC   99
100     114131  CodeB   FNC4    CodeB
101     311141  FNC4    CodeA   CodeA
102     411131  FNC1    FNC1    FNC1
103     211412  StartA  StartA  StartA
104     211214  StartB  StartB  StartB
105     211232  StartC  StartC  StartC
106     2331112 Stop    Stop    Stop
""".split()

VALUES = [int(value) for value in CODE128_CHART[0::5]]
WEIGHTS = dict(zip(VALUES, CODE128_CHART[1::5]))
CODE128A = dict(zip(CODE128_CHART[2::5], VALUES))
CODE128B = dict(zip(CODE128_CHART[3::5], VALUES))
CODE128C = dict(zip(CODE128_CHART[4::5], VALUES))


def get_128(a):
    final = {}
    for i in range(0, len(CODE128_CHART), 5):
        final[CODE128_CHART[i]] = CODE128_CHART[i+a]
    return final


C128A = get_128(2)
C128B = get_128(3)
C128C = get_128(4)



def decrypt(base64string):
    im = Image.open(BytesIO(base64.b64decode(base64string)))

    pix = im.load()

    fff = []

    # iterate pix
    for x in range(0, im.size[0], 11):
        r, g, b = pix[x, 0]
        # if r == 0:
        #     print("■", end="")
        # else:
        #     print(" ", end="")

        # print("({},0)".format(x), end="\t")

        final = ""
        blanc = 0
        noir = 0

        for d in range(x, x+11):
            if(d < im.size[0]):
                r, g, b = pix[d, 0]
                if r == 0:
                    print("■", end="")
                    if(blanc == 0):
                        noir += 1
                    else:
                        final += "{}".format(blanc)
                        blanc = 0
                        noir = 1
                else:
                    print("_", end="")
                    if(noir == 0):
                        blanc += 1
                    else:
                        final += "{}".format(noir)
                        blanc = 1
                        noir = 0
        if(noir != 0):
            final += "{}".format(noir)
        if(blanc != 0):
            final += "{}".format(blanc)

        id = [k for k, v in WEIGHTS.items() if v == final][0]
        print("\t", final, x, id, C128A[str(id)],
              C128B[str(id)], C128C[str(id)], sep="\t")
        fff.append(C128B[str(id)])
    return fff


class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):

        self.socket.send(data)

    def close(self):

        self.socket.close()


nc = Netcat('challenge.404ctf.fr', 30566)
first = True
while True:
    r = nc.read().decode("UTF-8")
    print("[READ]", r)
    b = 1 if first else 2
    if "Oh non" in r:
        print("ERROR !!!!!!!!!!!!!!")
        break
    base64s = r.split("\n")[b]
    print("[BASE64]", base64s)
    bb = decrypt(base64s)
    sended ="".join(bb)
    sended+="\n"
    nc.write(sended.encode('UTF-8'))
    print("[WRITE]", "".join(bb))
    first = False

nc.close()