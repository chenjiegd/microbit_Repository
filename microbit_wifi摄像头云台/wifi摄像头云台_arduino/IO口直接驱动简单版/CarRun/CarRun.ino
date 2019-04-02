/**
* @par Copyright (C): 2010-2019, Shenzhen Yahboom Tech
* @file         CarRun.c
* @author       liusen
* @version      V1.0
* @date         2018.05.07
* @brief       
* @details
* @par History  见如下说明
*
*/


/**
* Function       setup
* @author        liusen
* @date          2017.07.25
* @brief         初始化配置
* @param[in]     void
* @retval        void
* @par History   无
*/
void setup()
{
  //初始化电机驱动IO口为输出方式
  //串口波特率设置
  Serial.begin(9600);
  for(int i = 2; i < 14; i++)
  {
    pinMode(i, OUTPUT);
  }
 
}

/**
* Function       run
* @author        liusen
* @date          2017.07.25
* @brief         小车前进
* @param[in]     time
* @param[out]    void
* @retval        void
* @par History   无
*/
void run()
{

  digitalWrite(3, LOW);    //右电机前进禁止
  digitalWrite(2, HIGH);
  digitalWrite(4, LOW);    //右电机前进禁止
  digitalWrite(5, HIGH);
  
  digitalWrite(7, LOW);    //右电机前进禁止
  digitalWrite(6, HIGH);
  digitalWrite(8, LOW);    //右电机前进禁止
  digitalWrite(9, HIGH);
  
  
  digitalWrite(11, LOW);    //右电机前进禁止
  digitalWrite(10, HIGH);
  
  digitalWrite(12, LOW);    //右电机前进禁止
  digitalWrite(13, HIGH);
}

/**
* Function       brake
* @author        liusen
* @date          2017.07.25
* @brief         小车刹车
* @param[in]     time
* @param[out]    void
* @retval        void
* @par History   无
*/
void brake()
{
 for(int i = 2; i < 14; i++)
  {
    digitalWrite(i, LOW);
  }
}

/**
* Function       loop
* @author        liusen
* @date          2017.07.25
* @brief         先延时2，再前进1，后退1s,左转2s,右转2s,
*                原地左转3s,原地右转3s,停止0.5s
* @param[in]     void
* @retval        void
* @par History   无
*/

void loop()
{
  run();
  delay(1000);
  brake();
  delay(1000);

}


