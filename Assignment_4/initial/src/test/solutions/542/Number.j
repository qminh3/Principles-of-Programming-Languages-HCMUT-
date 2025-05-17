.source Number.java
.class public  Number
.super java.lang.Object
.implements Calc
.field a I
.field b I

.method public <init>(II)V
.var 0 is this LNumber; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label2:
	aload_0
	iload_2
	putfield Number/b I
	aload_0
	iload_2
	putfield Number/b I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LNumber; from Label0 to Label1
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

.method public add()V
.var 0 is this LNumber; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Number/a I
	aload_0
	getfield Number/b I
	iadd
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public multiply()V
.var 0 is this LNumber; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Number/a I
	aload_0
	getfield Number/b I
	imul
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
