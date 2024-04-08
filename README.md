# Speech Recognition
Sesi metne dönüştürme işlemini yapabilecek dört tane script var. Bunlardan biri Google API ile diğerleri ise Whisper API'ın farklı boyutları ile yazılmıştır. Bu projeyi yaparken edindiğim deneyimlere göre bu yazıyı yazıyorum.
Script'leri nasıl çalıştıracağınız ve çalıştırmadan önce neleri install etmeniz gerektiği aşağıda anlatılmıştır.

There are four scripts that can convert audio to text. One of them is written with Google API and the others are written with different dimensions of Whisper API. !! I am writing this article based on I gained experience while I was doing this project. 
How to run the scripts and what you need to install before running is explained below.

## Google API
Ses dosyalarını metne dönüştürme işlemini yapmak için kullanılan arayüzlerden biridir. Bu arayüzün kullanılabilmesi için “SpeechRecognition” kütüphanesinin kurulması gerekmektedir. 
Bu arayüz bazı ses kayıtlarını anlayamamaktadır. Anlayamadığı ses kayıtlarında, metin yerine exception hatası (UnknownValueError) yazmaktadır.

It is one of the APIs used to convert audio files to text. In order to use this API, the “SpeechRecognition” library must be installed. This API cannot understand some audio recordings. 
In voice recordings that it cannot understand, exception error (UnknownValueError) is written instead of text. (Free version used)

## Whisper API
Bu arayüz diğer arayüze göre daha kapsamlıdır ve doğruluk oranı daha yüksektir. Bu arayüzün kendi içinde beş tane boyutu bulunmaktadır. Bunlar tiny, base, small, medium ve large’dır. 
Bütün boyutlarda çoklu dil modeli bulunmaktadir. Yani aynı anda birden fazla dil için kullanılabilmektedirler. Buna ek olarak, istenirse large boyutu hariç diğer boyutlarda sadece ingilizce modeli de bulunmaktadır. 
Yani sadece İngilizce dili için de kullanılabilmektedir.  Bunun avantajı, İngilizce ses kaydını metne dönüştürme işlemi yaparken çoklu dil modeline göre doğruluk oranı daha yüksektir. 
Bu boyutlar arasındaki farklara gelecek olursak, her bir boyutun yaptığı dönüştürme işleminin doğruluk oranı öncekine göre daha yüksektir. Fakat doğruluk oranı arttıkça yapılan dönüştürme işleminin süresi de boyutun kullandığı 
VRAM’de artmaktadır. Yani tiny modelinin doğruluk oranı en düşük iken large modelinin doğruluk oranı en yüksektir. Buna karşın tiny modelinin dönüştürme işlemi süresi en kısa iken large modelinin dönüştürme işlemi en uzun süren işlemdir.
Aşağıda bulunan tabloda, boyutların parametre sayısına,  yaklaşık hız oranlarına ve kullandıkları VRAM’e bakabilirsiniz. 
![image](https://github.com/brkygn7/SpeechRecognition/assets/150448786/8c1d1b77-20ba-4b93-8dd6-e321dcb4083d)

Whisper API hakkında daha detaylı bilgi almak için [Whisper API](https://github.com/openai/whisper)

## Bleu Score
fsdvsfd

## Bilinmesi gerekenler
sdfsdfsd
## İnstall edilmesi gerekenler
