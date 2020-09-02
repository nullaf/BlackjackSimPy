import random
import time

gameCount = int(input("How many games of blackjack you want to simulate: "))
currentGameCount = 0
playerStop = 1

winCount = 0
loseCount = 0
drawCount = 0
inGame = 0

def pullCard():
  card = random.randrange(13)
  switcher = {
    0: "A",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "10",
    10: "J",
    11: "Q",
    12: "K"
  }
  card = switcher[card]
  return card

def cardSum(arr):
  i = 0
  j = 0
  totalSum = 0
  aCount = 0
  cardSwitcher = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10
  }
  for i in range(len(arr)):
    if(arr[i] == "A"):
      aCount += 1
    else:
      totalSum += cardSwitcher[arr[i]]

  allValues = []

  if(aCount == 0):
    allValues.append(totalSum)
    allValues.append(0)
  
  if(aCount > 0):
    allValues.append(totalSum + aCount)
    allValues.append(totalSum + aCount + 10)
  
  if(allValues[1] > 21):
    allValues[1] = 0

  if(allValues == []):
    return [totalSum,0]

  return allValues

def gameStart():
    global winCount,loseCount,drawCount
    dealerCards = []
    playerCards = []
    dealerCards.append(pullCard())
    playerCards.append(pullCard())
    inGame = 1
    while(inGame):
      while(max(cardSum(playerCards)) < playerStop):
        playerCards.append(pullCard())
        #print(f"Player: {playerCards}")
        if(cardSum(playerCards)[0] > 21):
          loseCount = loseCount + 1
          inGame = 0
          break
      if(not inGame):
        break
      while(max(cardSum(dealerCards)) < 17):
        dealerCards.append(pullCard())
        #print(f"Dealer: {dealerCards}")
        if(cardSum(dealerCards)[0] > 21):
          winCount = winCount + 1
          inGame = 0
          break
      if(not inGame):
        break
      if(max(cardSum(dealerCards)) > max(cardSum(playerCards))):
        loseCount = loseCount + 1
        inGame = 0
      elif(max(cardSum(dealerCards)) < max(cardSum(playerCards))):
        winCount = winCount + 1
        inGame = 0
      else:
        drawCount = drawCount + 1
        inGame = 0

dealerCards = []
playerCards = []

print("Player stops at\n ↓")
while(playerStop != 22):
  while(currentGameCount < gameCount):
    gameStart()
    currentGameCount = currentGameCount + 1
  print(f"({playerStop}) Win: {round((winCount/gameCount) * 100,3)}% , Lose: {round((loseCount/gameCount) * 100,3)}% , Draw: {round((drawCount/gameCount) * 100,3)}%")
  currentGameCount = 0
  winCount = 0
  loseCount = 0
  drawCount = 0
  playerStop = playerStop + 1


















