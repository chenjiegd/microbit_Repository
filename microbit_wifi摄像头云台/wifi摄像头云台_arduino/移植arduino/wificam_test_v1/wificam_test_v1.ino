//UART send 1~9==>20~180 degree
int servopin1=9;//设置舵机驱动脚到数字口9
int servopin2=10;//设置舵机驱动脚到数字口10
int myangle;//定义角度变量
int pulsewidth;//定义脉宽变量
int val;

#define run_car     '1'//按键前
#define back_car    '2'//按键后
#define left_car    '3'//按键左
#define right_car   '4'//按键右
#define stop_car    '0'//按键停

#define ON 1           //使能LED
#define OFF 0          //禁止LED

/*小车运行状态枚举*/
enum {
  enSTOP = 0,
  enRUN,
  enBACK,
  enLEFT,
  enRIGHT,
  enTLEFT,
  enTRIGHT
} enCarState;

/*串口数据设置*/
int IncomingByte = 0;            //接收到的 data byte
String InputString = "";         //用来储存接收到的内容
boolean NewLineReceived = false; //前一次数据结束标志
boolean StartBit  = false;       //协议开始标志
String ReturnTemp = "";          //存储返回值

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
    //串口波特率设置
    Serial.begin(9600);

	pinMode(servopin1,OUTPUT);//设定舵机接口为输出接口
	pinMode(servopin2,OUTPUT);//设定舵机接口为输出接口
}

void loop() {
    // put your main code here, to run repeatedly:
    servopulse(servopin1,val);//模拟产生PWM
    servopulse(servopin2,val);//模拟产生PWM

    if(NewLineReceived){
        serial_data_parse();  //调用串口解析函数
    }
}

/**
* Function       serial_data_parse
* @author        liusen
* @date          2017.07.25
* @brief         串口数据解析并指定相应的动作
* @param[in]     void
* @param[out]    void
* @retval        void
* @par History   无
*/
void serial_data_parse()
{

    //解析上位机发来的通用协议指令,并执行相应的动作
    //$4WD,PTZ180#
    if (InputString.indexOf("4WD") > 0)
    {
        //解析上位机发来的舵机云台的控制指令并执行舵机旋转
        //如:$4WD,PTZ180# 舵机转动到180度
        if (InputString.indexOf("PTZ") > 0)
        {
            int m_kp;
            int i = InputString.indexOf("PTZ"); //寻找以PTZ开头,#结束中间的字符
            int ii = InputString.indexOf("#", i);
            if (ii > i){
                String m_skp = InputString.substring(i + 3, ii);
                int m_kp = m_skp.toInt();        //将找到的字符串变成整型
                //Serial.print("PTZ:");
                //Serial.println(m_kp);
                
                SetServoPos(7, 180 - m_kp);//转动到指定角度m_kp
                //150 600   0-180
                //m_kp = map(180 - m_kp, 0, 180, SERVOMIN, SERVOMAX);
                // Serial.println(m_kp);
                //setServoPulse(7, SERVOMIN);
                
                InputString = "";                     //清空串口数据
                NewLineReceived = false;
                return;
            }
        }
    }
    //如:$1,0,0,0,0,0,0,0,0,0#    小车前进
    if(InputString.indexOf("4WD") == -1){
        //小车原地左旋右旋判断
        if(InputString[3] == '1'){      //小车原地左旋
            g_CarState = enTLEFT;
        }
        else if(InputString[3] == '2'){ //小车原地右旋
            g_CarState = enTRIGHT;
        }
        else{
            g_CarState = enSTOP;
        }
        //舵机左旋右旋判断
        if(InputString[9] == '1'){ //舵机旋转到180度
            SetServoPos(7, 180);//转动到指定角度
        }

        if(InputString[9] == '2'){ //舵机旋转到0度
            SetServoPos(7, 0);//转动到指定角度
        }

        //舵机归为判断
        if(InputString[17] == '1'){ //舵机旋转到90度
            SetServoPos(7, 90);//转动到指定角度
        }


        //小车加减速判断
        if(InputString[7] == '1'){     //加速，每次加50
            CarSpeedControl += 1000;
            if(CarSpeedControl > 4095){
                CarSpeedControl = 4095;
            }
        }
        if(InputString[7] == '2'){   //减速，每次减50
            CarSpeedControl -= 1000;
            if(CarSpeedControl < 0){
                CarSpeedControl = 500;
            }
        }
        //小车的前进,后退,左转,右转,停止动作
        if(g_CarState != enTLEFT && g_CarState != enTRIGHT){
            switch (InputString[1]){
                case run_car:   g_CarState = enRUN;  break;
                case back_car:  g_CarState = enBACK;  break;
                case left_car:  g_CarState = enLEFT;  break;
                case right_car: g_CarState = enRIGHT;  break;
                case stop_car:  g_CarState = enSTOP;  break;
                default: g_CarState = enSTOP; break;
            }
        }

        InputString = "";         //清空串口数据
        NewLineReceived = false;

        //根据小车状态做相应的动作
        switch(g_CarState){
            case enSTOP: brake(); break;
            case enRUN: run(CarSpeedControl); break;
            case enLEFT: left(CarSpeedControl); break;
            case enRIGHT: right(CarSpeedControl); break;
            case enBACK: back(CarSpeedControl); break;
            case enTLEFT: spin_left(CarSpeedControl); break;
            case enTRIGHT: spin_right(CarSpeedControl); break;
            default: brake(); break;
        }
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

void serialEvent()
{
    while (Serial.available()){
        //一个字节一个字节地读,下一句是读到的放入字符串数组中组成一个完成的数据包
        IncomingByte = Serial.read();
        if (IncomingByte == '$'){
            StartBit = true;
        }
        if (StartBit == true){
            InputString += (char) IncomingByte;
        }
        if (IncomingByte == '#'){
            NewLineReceived = true;
            StartBit = false;
        }
    }
}
