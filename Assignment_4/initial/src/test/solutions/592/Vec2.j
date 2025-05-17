.source Vec2.java
.class public  Vec2
.super java/lang/Object
.field public x I
.field public y I

.method public <init>(II)V
.var 0 is this LVec2; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Vec2/x I
	aload_0
	iload_2
	putfield Vec2/y I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LVec2; from Label0 to Label1
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

.method public lengthSquared()I
.var 0 is this LVec2; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Vec2/x I
	aload_0
	getfield Vec2/x I
	imul
	aload_0
	getfield Vec2/y I
	aload_0
	getfield Vec2/y I
	imul
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
