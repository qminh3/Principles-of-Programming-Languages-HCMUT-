.source Pair.java
.class public  Pair
.super java.lang.Object
.field x I
.field y I

.method public <init>(II)V
.var 0 is this LPair; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
Label2:
	aload_0
	iload_2
	putfield Pair/y I
	aload_0
	iload_2
	putfield Pair/y I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LPair; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
