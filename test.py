import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = 'とりあえずmacでMeCabが動きました。'

print(mecab.parse(text))

"""
# 実行結果

とりあえず	副詞,助詞類接続,*,*,*,*,とりあえず,トリアエズ,トリアエズ
mac	名詞,固有名詞,一般,*,*,*,MAC,マック,マック
で	助詞,格助詞,一般,*,*,*,で,デ,デ
MeCab	名詞,固有名詞,一般,*,*,*,MeCab,メカブ,メカブ
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
動き	動詞,自立,*,*,五段・カ行イ音便,連用形,動く,ウゴキ,ウゴキ
まし	助動詞,*,*,*,特殊・マス,連用形,ます,マシ,マシ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。	記号,句点,*,*,*,*,。,。,。
EOS
"""