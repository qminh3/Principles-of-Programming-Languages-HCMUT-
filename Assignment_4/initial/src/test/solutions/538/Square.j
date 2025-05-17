.source Square.java
.class public  Square
.super java.lang.Object
.implements Shape
.field side I

.method public <init>(I)V
.var 0 is this LSquare; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is side I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Square/side I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LSquare; from Label0 to Label1
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

.method public area()V
.var 0 is this LSquare; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Square/side I
	aload_0
	getfield Square/side I
	imul
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
