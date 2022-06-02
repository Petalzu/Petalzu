object helloworld {
  def main(args: Array[String]): Unit = {
    println("hello world")
  }
}
/*
区分大小写 -  Scala是大小写敏感的，这意味着标识Hello 和 hello在Scala中会有不同的含义。

类名 - 对于所有的类名的第一个字母要大写。
如果需要使用几个单词来构成一个类的名称，每个单词的第一个字母要大写。
eg：class MyFirstScalaClass

方法名称 - 所有的方法名称的第一个字母用小写。
如果若干单词被用于构成方法的名称，则每个单词的第一个字母应大写。
eg：def myMethodName()

程序文件名 - 程序文件的名称应该与对象名称完全匹配(新版本不需要了，但建议保留这种习惯)。
保存文件时，应该保存它使用的对象名称（记住Scala是区分大小写），并追加".scala"为文件扩展名。 （如果文件名和对象名称不匹配，程序将无法编译）。
eg: 假设"HelloWorld"是对象的名称。那么该文件应保存为'HelloWorld.scala"

def main(args: Array[String]) - Scala程序从main()方法开始处理，这是每一个Scala程序的强制程序入口部分。
*/
//单行注释

object huanhang{
  def main(args: Array[String]): Unit = {
    val s = "hello"; println(s)//换行符
  }
}

package com.runoob{//定义包
  class HelloWorld
}