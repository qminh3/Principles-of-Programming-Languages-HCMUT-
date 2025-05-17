.source PPL.java
.class public  PPL
.super java.lang.Object
.implements Course
.field number I

.method public <init>(I)V
.var 0 is this LPPL; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is number I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield PPL/number I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LPPL; from Label0 to Label1
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

.method public exam()V
.var 0 is this LPPL; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield PPL/number I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
