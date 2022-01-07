import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    word = input()

    if K > len(word):
        print('#{} {}'.format(tc, 'none'))

    else:
        suffix = sorted([word[i:] for i in range(0, len(word))])
        print('#{} {}'.format(tc, suffix[K-1]))


#1 onster
#2 n
#3 isticexpialidocious
#4 xqkixrxdelzxvcylocxtmwu
#5 otomonstrosesquippedaliophobia
#6 noconiosis
#7 kyewrkjgcetbdlxjkfboezjzhephuugzlqzbeuiiuwucwzgowduazjombimjptzpfztklu
#8 lobvbqjezkheifdwdouwosciuupcdgniznfnqdlmsckefn
#9 nfnqdlmsckefnpnriuwlnnxdzzorbpjjwhgzvumymslqvktsxuisacmwogfmobxgckcsidythaewxzskxhpfnkygvlhaipiqkbynfvbuomqtdjdnceupgusgznecpeviidnqrbghfpzoktuwhygwizyogffsjytsyiukogjxuhfszombbidhncmbgrbbryrpudlnukhpaoxrimaomhdpvyvzkqtzvlxvtkmrcilltssmxiepqyvodcwepahxrolwkfbeqdtbvvfpq
#10 scofsarulkpkncnotjioonwwtbmtrfrbizzaelsofdstuzfepimejxipwvmwnsdbiqwdmohcqnswxcpdecjvildcrofjcfhcjiwcynvkgalswnvivhakxnrfeasymuvlpyzxdwbmazjoauepxetkpvwzsfvwkgrojsfcedgvgdgqebwanhozynbwcvovasdciowvckoroeesuxsgczrbztrktitnvpblhvemmjesnfnltvmzodsiknkeguqmkzjlzcbbdluzvhhfzbbhabnfwlrqnfspacvpharaizgkteuelezbejipwoavulaxajrjkvpttkmmuyrgxblyjcgmfldvmnuoerftaxnnrkgtavuasyjijotyemwm