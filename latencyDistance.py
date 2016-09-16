def latencyDistance():
    speedOfLight = 300000
    lightbulbLatency = 1
    cpuLatency = 0.4
    dramLatency = 12
    nanoSecond = 1000000000
    dramLatencyDinMeter = speedOfLight*1000/nanoSecond*dramLatency
    
    hardLatency = 7 # hard drive Latency is 7 mili seconds
    miliSecond = 100
    perTeraPrice = 100 * 1,000,000,000

    hardLatencyDinKilo = speedOfLight/miliSecond*dramLatency
    hardCostNanoDollars = 100* 1,000,000,000
    a = 1
    print (a)
    

