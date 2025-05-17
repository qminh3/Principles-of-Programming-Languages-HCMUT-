.source Limit.java
.class public  Limit
.super java.lang.Object
.implements Stepper
.field count I

.method public <init>(I)V
.var 0 is this LLimit; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is count I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Limit/count I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LLimit; from Label0 to Label1
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

.method public done(I)Z
.var 0 is this LLimit; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
Label2:
	iload_1
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
.limit locals 2
.end method
