.source Checker.java
.class public  Checker
.super java.lang.Object
.field done Z
.field count I

.method public <init>(ZI)V
.var 0 is this LChecker; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is done Z from Label0 to Label1
.var 2 is count I from Label0 to Label1
Label2:
	aload_0
	iload_2
	putfield Checker/count I
	aload_0
	iload_2
	putfield Checker/count I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LChecker; from Label0 to Label1
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
