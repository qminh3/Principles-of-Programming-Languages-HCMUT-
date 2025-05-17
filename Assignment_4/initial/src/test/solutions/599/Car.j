.source Car.java
.class public  Car
.super java.lang.Object
.implements Engine
.field speed I

.method public <init>(I)V
.var 0 is this LCar; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is speed I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Car/speed I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCar; from Label0 to Label1
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

.method public rpm()I
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Car/speed I
	bipush 100
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
