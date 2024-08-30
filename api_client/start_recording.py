from src.RemoteControl import RemoteControl

HOST = '192.168.1.103'  # One Plus IP address in JioFi


def main():
    # example class usage
    # constructor starts the connection
    remote = RemoteControl(HOST)
    print("Connected")
    
    #print("Magnetometer data length: %d" % len(magnetic_data))
    #with open("magnetic.csv", "w+") as imu_file:
    #    imu_file.writelines(magnetic_data)
    
    phase, duration, exp_time = remote.start_video()
    print("%d %f" % (exp_time, duration))
    # time.sleep(5)
    _=input("Press enter/return to stop recording: ")
    
    remote.stop_video()

    # receives last video (blocks until received)
    # start = time.time()
    # filename = remote.get_video(want_progress_bar=True)
    # end = time.time()
    # print("elapsed: %f" % (end - start))
    print('Closing connection')
    remote.close()


if __name__ == '__main__':
    main()
