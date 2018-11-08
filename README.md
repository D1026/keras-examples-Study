# keras-examples-Study
# ---------- 2018.11.08 --------------
---- babi_memnn.py ----     
1、embedding M（记忆网络的story嵌入） 和 embedding Q（问题嵌入）不是同一个嵌入，也就是说他们的 { index ： vector}
    字典表可能根本不一致，两个坐标系不同的词嵌入空间，用点积 来度量 两个响亮的相似/相关程度，是没有意义的