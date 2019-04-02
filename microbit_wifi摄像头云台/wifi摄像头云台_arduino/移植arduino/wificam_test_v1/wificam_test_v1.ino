//UART send 1~9==>20~180 degree
int servopin1=9;//设置舵机驱动脚到数字口9
int servopin2=10;//设置舵机驱动脚到数字口10
int myangle;//定义角度变量
int pulsewidth;//定义脉宽变量
int val;
void servopulse(int servopin,int myangle)/*定义一个脉冲函数，用来模拟方式产生PWM值*/
{
    pulsewidth=(myangle*11)+500;//将角度转化为500-2480的脉宽值
    digitalWrite(servopin1,HIGH);//将舵机接口电平置高
    delayMicroseconds(pulsewidth);//延时脉宽值的微秒数
    digitalWrite(servopin1,LOW);//将舵机接口电平置低
    delay(20-pulsewidth/1000);//延时周期内剩余时间
}

void setup() {
    // put your setup code here, to run once:
	pinMode(servopin1,OUTPUT);//设定舵机接口为输出接口
	pinMode(servopin2,OUTPUT);//设定舵机接口为输出接口
}

void loop() {
    // put your main code here, to run repeatedly:
    servopulse(servopin1,val);//模拟产生PWM
}