import asyncio
from julabo import JulaboCF, connection_for_url


async def main():
    # Connect directly to USB serial device
    conn = connection_for_url("serial:///dev/ttyACM0", baudrate=9600)
    dev = JulaboCF(conn)
    await conn.open()

    ident = await dev.identification()
    status = await dev.status()
    print(f"{ident} status is: {status}")

    # read temperature:
    temp = await dev.bath_temperature()
    print(f"Bath temperature: {temp} degC")

    # start the device
    started = await dev.is_started()
    if not started:
       await dev.start()

    # define a new set point
    await dev.set_point_1(34.56)

asyncio.run(main())