/**
* @par Copyright (C): 2010-2019, Shenzhen Yahboom Tech
* @file         CarRun.c
* @author       liusen
* @version      V1.0
* @date         2017.07.25
* @brief       小车前进后退左右综合实验
* @details
* @par History  见如下说明
*
*/
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);
#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)


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
    pwm.begin();
  
    pwm.setPWMFreq(50);  // Analog servos run at ~60 Hz updates
}

/**
* Function       SetServoPos
* @author        liusen
* @date          2018.05.07
* @brief         初始化配置
* @param[in]     num: 舵机的编号； value：舵机角度：0-180
* @retval        void
* @par History   无
*/
void SetServoPos(int num, int value)
{
    // 50hz: 20,000 us
    long us = (value * 1800 / 180 + 600); // 0.6 ~ 2.4
    long pwmvalue = us * 4096 / 20000;
    pwm.setPWM(num, 0, pwmvalue);
}

/**
* Function       loop
* @author        liusen
* @date          2017.07.25
* @brief        
*                
* @param[in]     void
* @retval        void
* @par History   无
*/

void loop()
{

    SetServoPos(0, 90);//K9
    SetServoPos(1, 90);//K10
    SetServoPos(2, 90);//K11
    SetServoPos(3, 90);//K12
    SetServoPos(4, 90);//K13
    SetServoPos(5, 90);//K14
    SetServoPos(6, 90);//K15
    SetServoPos(7, 90);//K16

}
