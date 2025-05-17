.source Counter.java
.class public  Counter
.super java/lang/Object
.field public value I

.method public <init>(I)V
.var 0 is this LCounter; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is value I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Counter/value I
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCounter; from Label0 to Label1
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

.method public inc()I
.var 0 is this LCounter; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Counter/value I
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public triple()I
.var 0 is this LCounter; from Label0 to Label1
Label0:
Label2:
	aload_1
	invokevirtual Counter/inc()I
	iconst_3
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
