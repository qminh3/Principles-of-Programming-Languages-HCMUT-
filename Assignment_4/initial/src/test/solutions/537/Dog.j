.source Dog.java
.class public  Dog
.super java.lang.Object
.implements Animal
.field sound Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LDog; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is sound Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Dog/sound Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LDog; from Label0 to Label1
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

.method public speak()V
.var 0 is this LDog; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Dog/sound Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
