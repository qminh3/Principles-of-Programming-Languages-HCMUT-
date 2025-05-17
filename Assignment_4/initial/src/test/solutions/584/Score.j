.source Score.java
.class public  Score
.super java/lang/Object
.field public math I
.field public english I

.method public <init>(II)V
.var 0 is this LScore; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is math I from Label0 to Label1
.var 2 is english I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Score/math I
	aload_0
	iload_2
	putfield Score/english I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LScore; from Label0 to Label1
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

.method public average()I
.var 0 is this LScore; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Score/math I
	aload_0
	getfield Score/english I
	iadd
	iconst_2
	idiv
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
