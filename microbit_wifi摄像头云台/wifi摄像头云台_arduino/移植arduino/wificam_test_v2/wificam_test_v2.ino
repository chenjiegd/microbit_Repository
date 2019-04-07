/**
* @par Copyright (C): 2010-2019, Shenzhen Yahboom Tech
* @file         wificam_arduino
* @author       wusicaijuan(五丝菜卷)
* @version      V1.0
* @date         2019.04.03
* @brief        wifi摄像头_arduino
* @details
* @par History  见如下说明
*
*/
/*串口数据设置*/
int IncomingByte = 0;            //接收到的 data byte
String InputString = "";         //用来储存接收到的内容
boolean NewLineReceived = false; //前一次数据结束标志
boolean StartBit  = false;       //协议开始标志

void setup() {
	// put your setup code here, to run once:
	//串口波特率设置
    Serial.begin(9600);
}

void loop() {
	// put your main code here, to run repeatedly:

}

void servopulse(int servopin,int myangle)/*定义一个脉冲函数，用来模拟方式产生PWM值*/
{
    pulsewidth=(myangle*11)+500;//将角度转化为500-2480的脉宽值
    digitalWrite(servopin1,HIGH);//将舵机接口电平置高
    delayMicroseconds(pulsewidth);//延时脉宽值的微秒数
    digitalWrite(servopin1,LOW);//将舵机接口电平置低
    delay(20-pulsewidth/1000);//延时周期内剩余时间
}

void serial_data_parse(){
	//解析上位机发来的通用协议指令,并执行相应的动作
	//$4WD,PTZ180#
	if(InputString.indexOf("4WD") > 0){
		//解析上位机发来的舵机云台的控制指令并执行舵机旋转
		//如:$4WD,PTZ180# 舵机转动到180度
		if(InputString.indexOf("PTZ") > 0){
			int m_kp;
			int i = InputString.indexOf("PTZ"); //寻找以PTZ开头,#结束中间的字符
			int ii = InputString.indexOf("#", i);
			if (ii > i){
				String m_skp = InputString.substring(i + 3, ii);
				int m_kp = m_skp.toInt();        //将找到的字符串变成整型
				SetServoPos(7, 180 - m_kp);//转动到指定角度m_kp
				InputString = "";
				NewLineReceived = false;
				return;	
			}
		}
	}
	//如:$1,0,0,0,0,0,0,0,0,0#    小车前进
	if(InputString.indexOf("4WD") == -1){

	}
}

/**
* Function       serialEvent
* @author        liusen
* @date          2017.07.25
* @brief         串口解包
* @param[in]     void
* @param[out]    void
* @retval        void
* @par History   无
*/

void serialEvent(){
	while (Serial.available()){
		//一个字节一个字节地读,下一句是读到的放入字符串数组中组成一个完成的数据包
		IncomingByte = Serial.read();
		if(IncomingByte == '$'){
			StartBit = true;
		}
		if(StartBit == true){
			InputString += (char) IncomingByte;
		}
		if(IncomingByte == '#'){
			NewLineReceived = true;
			StartBit = false;
		}
	}
}