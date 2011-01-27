#!/usr/bin/env python
# -*- coding: utf-8 -*-

import languageIdentifier

languageIdentifier.load("/Users/jgraves/trigrams/")
print languageIdentifier.identify("This is a short english string?", 300, 300), "English"
print languageIdentifier.identify("ليل مواقع احبك موت,دردشة,شات,منتديات,احبك,منتدى,دلي", 300, 300), "Arabic"
print languageIdentifier.identify("La vitamina A o retinol es una vitamina o un calcio liposoluble; ayuda a la formación y mantenimiento de dientes sanos y tejidos blandos y óseo", 300, 300), "Spanish"
print languageIdentifier.identify("Á, ou A accent aigu, est un graphème utilisé dans les alphabets féringien, hongrois, islandais, slovaque et tchèque en tant que lettre et dans les alphabets", 300, 300), "French"
print languageIdentifier.identify("Первый Альтернативный Музыкальный Телеканал - альтернативная музыка, новости музыки, клипы, форум о музыке.", 300, 300), "Russian"
print languageIdentifier.identify("Die Übersetzung der Präposition à hängt stark von dem jeweiligen Kontext ab. Da im Französischen nicht dekliniert wird,", 300, 300), "German"
print languageIdentifier.identify("這是具有歷史意義的一部A 片（雖然不是我們的歷史～）; 有劇情（雖然我覺得A 片幹嘛要有劇情？哪個人看A 片會像看電影", 300, 300), "Chinese"
print languageIdentifier.identify("ラテン文字（アルファベット）の1番目の文字。小文字は a 。ギリシャ文字のΑ（アルファ）に由来し、キリル文字のАに相当する ... この文字が表す音素は原則として[a]（非円唇前舌広母音）もしくは[ɑ]（非円唇後舌広母音", 300, 300), "Japanese"
print languageIdentifier.identify("lettera dell'alfabeto latino e italiano e anche nella maggior parte degli alfabeti derivanti da quello fenicio.", 300, 300), "Italian"
print languageIdentifier.identify("선박 운송 전문업체, 서비스 포트정보와 해외지사 소개, 운항스케쥴, 고객 서비스 제공.", 300, 300), "Korean"
print languageIdentifier.identify("Det gemena a:et finns utformat i två versioner (allografer): det så kallade envånings-a:et med en våning (ɑ) och det så kallade tvåvånings-a:et med två", 300, 300), "Swedish"
print languageIdentifier.identify("A ni herufi ya kwanza katika alfabeti ya Kilatini ambayo ni pia mwandiko wa Kiswahili cha kisasa. Asili yake ni Alfa ya Kigiriki.", 300, 300), "Swahili"
print languageIdentifier.identify("Å je písmeno v abecedě některých jazyků (švédština, finština, dánština, norština, severofríština, valonština, chamorro, istro-románské jazyky), kde označuje", 300, 300), "Czech"
print languageIdentifier.identify("What is a paradigm? In my own words, a paradigm is a belief system. It can be a personal belief system, or one held by a mass number of people, or even the whole world. Such a belief system is so entrenched in our minds as truth that it usually does not occur to us to question it. Therefore, many of us never even think that maybe this thought pattern needs updating. But, inevitably there are those that go against the common thought, and begin to challenge long held beliefs. More and more people begin to awaken, each individual begins to change their personal belief system, and the phenomenon that occurs as this old belief system comes tumbling down is often referred to as a paradigm shift", 300, 300), "English"
