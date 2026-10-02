# SnakeAI
DQL Learning


# Algoritma
```python
                 SNAKE OYUNU
                     │
                     ▼
                   STATE
                     │
                     ▼
              ┌─────────────┐
              │ Neural Net  │
              └──────┬──────┘
                     │
              Q değerleri
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        SOL       DÜZ       SAĞ
          │          │          │
          └──────────┼──────────┘
                     ▼
                  ACTION
                     │
                     ▼
                OYUN ÇALIŞIR
                     │
              ┌──────┴──────┐
              ▼             ▼
            REWARD      NEW STATE
              │             │
              └──────┬──────┘
                     ▼
                 ÖĞRENME
                     │
                     └──────► tekrar           
```



# # Reinforcement Learning
**AGENT** -> YILAN AI

**ENVIRONMENT** -> YILAN OYUNU

**STATE** -> YILANIN VE YEMEĞİN MEVCUT DURUMU

**ACTION** -> SOL DÜZ SAĞ

**REWARD** -> YEDİ ÖLDÜ VS.

**EPISODE** -> BİR OYUNUN BAŞINDAN ÖLÜMÜNE KADAR

----

Agent = 🐍
Environment = 🎮 Snake
***
STATE -> ACTION -> ENVIRONMENT -> REWARD -> NEW STATE
***

# KONULAR
State Nedir?
- AI' ın dünyayı nasıl gördüğünü biz belirliyoruz
- Örnek AI'a ekranın tamamını vermek zorunda değiliz.
```
████████████
█          █
█    🍎    █
█     🐍   █
█          █
████████████
```
- Başlangıç için daha basit yapılabilir.
```
danger_straight
danger_riht
danger_left

direction_up
direction_down
direction_right
direction_left

food_up
food_down
food_right
food_left
```

- Örnek
```python
state = [
    1, # straight danger
    0, # right danger
    0, # left danger

    1, # moving up
    0, # moving down
    0, # right
    0, # left

    1, # food up
    0, # food down
    0, # food right
    0 # food left
]
```
- Burada 11 adet input olduğunu görebiliriz.
- AI bu dünyayı görüyor
***
Action Nedir?
- AI'ın yapabileceği hareketlerdir.
- Örnek:
````
0 -> SOL
1 -> DÜZ
0 -> SAĞ
````
- Yapabiliriz
- Dolayısıyla Neural Network:
````
11 input -> Neural Network -> 3 output
````
- Verecektir.

````
SOL   = 2.1
DÜZ   = 7.8
SAĞ   = 1.3
````
*AI burada **DÜZ** olanı seçecektir.*

***
Reward Nedir?
- AI' a nasıl davranmasını gerektiğini **reward** ile öğretiyoruz.
- Örneğin:
````python
if ate_food:
    reward += 10

elif died:
    reward -= 10

else:
    reward = 0
````
- Ama burada çok önemli bir problem var.
````
AI sadece:

Yemek = +10
Ölüm = -10

bilirse bazen saçma hareketler yapabilir.

Bu yüzden daha sonra reward sistemini biraz daha akıllı yapabiliriz.

Mesela yemeğe yaklaşırsa:

+0.1

uzaklaşırsa:

-0.1

gibi.

Ama ilk versiyonda bunu basit tutacağız.
````
***
Episode Nedir?
- Episode bir oyundur.
````
Episode 1

START
 ↓
oyna
 ↓
oyna
 ↓
yemek
 ↓
oyna
 ↓
öl

...

Episode 1
Episode 2
Episode 3
...
Episode 10000


````
***
Q  Nedir?
- Bu durumda bu hareketi yaparsam en kadar iyi sonuç bekliyorum demeyi ifade eder.
- Örnek:
````
State: 
Yemek Sağda
Önüm Boş
Solum Duvar

AI:
SOL Q = -5
DÜZ Q = 2
SAĞ Q = 8

Olarak görmektedir.

AI "SAĞ" sonucunu seçmektedir.
````

Burada önemli bir detay Q değerini Neural Network veriyor ama başlangıçta Neural Network hiçbişey bilmiyor binlerce deney sonrasında öğreniyor
***
DQL Nedir
- DQL neden Deep sorusuna gelecek olursak klasik Q-learning de Q-table olabilir.
- state -> action -> Q
- Ama snake oyununun uzayı büyüdükçe tablo devasa olur
- Neural Network kullanıyoruz bu yüzden Deep Q-learning diyoruz
***
Bellman Equation (Matematik) Nedir?
- Dışarıdan okununca korkulacak bişey olsa bile mantığı oldukça basittir.
- Temel fikir:
````
Yeni Tahmin = şimdiki ödül + gelecekteki beklenen ödül

Matematiksel formülü:

Q(s,a)=r+γmaxQ(s′,a′)
şeklindedir.

s  = mevcut state
a  = yaptığımız action
r  = aldığımız reward
s' = yeni state
γ  = discount factor

Örnek:
Reward = +10
Gelecekteki Q = 8
Gamma = 0.9

10 + 0.9 × 8 = 17.2

Bu hareketin yaklaşık değeri 17.2 olmalı.


````

***
Loss Nedir?
- Network bir tahmin yapıyor:
````
Tahmin = 12
````
- Ama bizim hesapladığımız target:
````
target = 17.5
````
- Aradaki fark:
````
17.2 - 12 = 5.2
````

Network yanlış tahmin yaptım diyerek ağırlıkları güncelliyor bu farkı ölçmek içinde loss function kullanıyoruz
````
loss
 ↓
backpropagation
 ↓
gradient
 ↓
weights update
````
***
Experience Replay Nedir?
- DQN'in önemli parçalarından biridir.
- AI her deneyimini kaydediyor:
````
(state,
 action,
 reward,
 next_state,
 done)

ÖRNEK:
(
 [1,0,0,...],
 2,
 10,
 [0,0,0,...],
 False
)

Bunları memory de tutuyoruz



Memory:

Experience 1
Experience 2
Experience 3
...
Experience 100000

````
- Sonra rastgele bir batch çekiyoruz
````
32 deneyim
````
ve networkü bunlarla eğitiyoruz

- Buradaki batch rastgele seçilme sebebi AI'ın ardışık deneyimlere aşırı bağımlı olmasını engellemek

*** 
Exploration vs Exploitation Nedir?
- AI'ın iki seçeneği var

Exploitation: *Şu ana kadar öğrendiğim en iyi hareketi yapayım*

Exploration: *Acaba başka hareket daha iyimi*

Örneğin:
````
epsilon = 0.1
````
ise kabaca
````
%10 rastgele harekete
%90 öğrendiğim en iyi hareket
````
- Training ilerledikçe 
````
epsilon
1.0
 ↓
0.9
 ↓
0.7
 ↓
0.4
 ↓
0.1
````
gibi azaltılabilir.
***
Discount Factor -Y Nedir?
- Bu da AI ın geleceğe ne kadar önem verdiğini belirler.
- Örneğin:
````
gamma = 0.9
ise gelecek önemli.
gamma = 0.1
ise AI daha çok "Şu anda ne kazandım" diye düşünür
````
***
Target Network Nedir?
- DQN'in önemli parçalarından biridir.
- İki network kullanıyoruz:
````
Policy Network
Target Network

              State
                │
        ┌───────┴───────┐
        ▼               ▼
 Policy Network    Target Network
        │               │
        ▼               ▼
   prediction         target

Target network daha yavaş güncelleniyor.

Bu eğitim stabilitesini artırıyor.

İlk Snake versiyonunda bunu biraz sonra ekleyeceğiz.

````
***
Algoritma Nasıl İşleyecek?
````
FAZ 1
Snake oyununu yaz
        ↓
FAZ 2
State sistemini yaz
        ↓
FAZ 3
Random Agent
        ↓
FAZ 4
Reward sistemi
        ↓
FAZ 5
Neural Network
        ↓
FAZ 6
Q-Learning
        ↓
FAZ 7
Experience Replay
        ↓
FAZ 8
DQN
        ↓
FAZ 9
Training
        ↓
FAZ 10
Model kaydetme
        ↓
FAZ 11
Grafik / TensorBoard
        ↓
FAZ 12
Eğitilmiş modeli oynat
````
