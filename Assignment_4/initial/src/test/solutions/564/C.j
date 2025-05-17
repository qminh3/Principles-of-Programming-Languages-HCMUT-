.source C.java
.class public  C
.super java.lang.Object
.implements Looper
.field count I

.method public <init>(I)V
.var 0 is this LC; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is count I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield C/count I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LC; from Label0 to Label1
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

.method public done()Z
.var 0 is this LC; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield C/count I
	iconst_3
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
