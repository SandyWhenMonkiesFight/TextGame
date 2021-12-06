Healthy = 50
TotalHealthy = 50
MaxTotal = 100

def GetHealth():
    global Healthy
    return Healthy

def GetMaxH():
    global TotalHealthy
    return TotalHealthy

def Health():
    global Healthy
    global TotalHealthy
    print("Health = ",Healthy,"/",TotalHealthy)

def loseHealth(Val):
    global Healthy
    if Healthy-Val > 0:
        Healthy -= Val
    else:
        Health = 0

def gainHealth(Val):
    global Healthy
    global TotalHealthy
    if Healthy+Val < TotalHealthy:
        Healthy += Val
    else:
        Healthy = TotalHealthy

def HMax(Val):
    global TotalHealthy
    global MaxTotal
    if TotalHealthy+Val < MaxTotal:
        TotalHealthy += Val
    else:
        TotalHealthy = MaxTotal
    
    
def Hmin(Val):
    global TotalHealthy
    if TotalHealthy-Val > 1:
        TotalHealthy -= Val
    else:
        TotalHealthy = 0
