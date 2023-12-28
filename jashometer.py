# JASHOMETER COMPARISONS TO IMPERIAL MEASUREMENT SYSTEM

# 1 jashometer = 5f 11in OR 71in OR 5.91FT OR 1.80m 

m = float(1.8034)
ft = float(5.9166667)
inc = float(71)

print("JASHOMETER CALCULATOR!! \n")

operation = input(
    "choose an option: \n 1- meters to jashometers \n 2- feet & inches to jashometers \n 3- jashometers to meters and feet&inches \n"
                  )

if operation == "1":
    a = float(input(
        "* enter the length in meters: * \n" 
    ))
  
    jm = a / m

    print(
        "* qm, quadrapedalmeter: *", jm * 1000,
        "\n him, himmeter:", jm * 100,
        "\n cm, chonnymeter:", jm * 10,
        "\n jm, jashometer:", jm,
        "\n sm, soulmeter:", jm * 0.1,
        "\n mim, mindmeter:", jm * 0.01,
        "\n hm, heartmeter:", jm * 0.001
    )
  
elif operation == "2":
    a = float(input(
        "enter the length in feet: \n"
    ))

    b = float(input("enter the length in inches:\n"))

    jm = (a / ft) + (b / inc)

  
    print(
        "* qm, quadrapedalmeter: *", jm * 1000,
        "\n him, himmeter:", jm * 100,
        "\n cm, chonnymeter:", jm * 10,
        "\n jm, jashometer:", jm,
        "\n sm, soulmeter:", jm * 0.1,
        "\n mim, mindmeter:", jm * 0.01,
        "\n hm, heartmeter:", jm * 0.001
    )
  
elif operation == "3":
    c = float(input("enter the length in jashometers (jm):\n"))

    mj = float(c * m)
    ftj = float(c * ft)
    incj = float(c * inc)

    print("meters:  ", mj, "\n feet:  ", ftj, "\n inches:  ", incj)

else:
    print("invalid operation")

d = input()
