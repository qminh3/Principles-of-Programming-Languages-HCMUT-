.source Num.java
.class public  Num
.super java.lang.Object
.implements Power
.field val I

.method public <init>(I)V
.var 0 is this LNum; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Num/val I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LNum; from Label0 to Label1
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

.method public square()I
.var 0 is this LNum; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Num/val I
	aload_0
	getfield Num/val I
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
