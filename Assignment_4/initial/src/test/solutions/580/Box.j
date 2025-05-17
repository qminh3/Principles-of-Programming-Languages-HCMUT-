.source Box.java
.class public  Box
.super java.lang.Object
.field width I
.field height I

.method public <init>(II)V
.var 0 is this LBox; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is width I from Label0 to Label1
.var 2 is height I from Label0 to Label1
Label2:
	aload_0
	iload_2
	putfield Box/height I
	aload_0
	iload_2
	putfield Box/height I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LBox; from Label0 to Label1
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

.method public area()I
.var 0 is this LBox; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Box/width I
	aload_0
	getfield Box/height I
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
