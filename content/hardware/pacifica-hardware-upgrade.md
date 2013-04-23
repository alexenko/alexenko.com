Title: pacifica hardware upgrade
Date: 2010-08-29 12:29
Author: Alexenko
Category: Hardware
Tags: bargain, debian, hardware, pacifica

Some time ago I decided to upgrade pacifica, my home server. Currently
it's running on an Athlon 2200+. It's sufficient for most tasks but
during CPU intensive operations it shows its age. The two SATA ports on
the mobo are also not sufficient at some point would force me to replace
it anyways.

<!--more-->

I set myself a hard budget cap of \$200. No matter what I wasn't going
to go over that limit. I would count the price AFTER MIRs (Mail In
Rebates) though. [Fractal Design R2][] is what's currently used as it's
sexy, quiet, and has plenty of space for hdds. It's bent in a lot of
places and the front panel keeps falling off because it was dropped
during shipping and most of the plastic pins broke. Yay for shipping
insurance though as the case was free. The new hardware would go into
the same case, but I would need a new case to move the old hardware into
(it's going to be a box for my parent's house so that I can admin their
network from home). Thus I needed to purchase a case, mobo, CPU, RAM,
and PSU, all for \$200. A HDD currently unused in the server would be
used for the OS. Since I was on a such strict budget I had to wait for
special sales. It took a while (I think over a month) but between
[slickdeals.net][] and [newegg.com][] sales (guerilla, shell shocker,
etc.) I finally found all of the parts for the price I was willing to
pay. I wanted an X3 cpu and unlock the 4th core, but that was way over
budget.

I settled on the following hardware thanks to
[hardware.reddit][]/[buildapc.reddit][] and this [awesome chart from
paulisageek.com][]

-   Motherboard + CPU Combo special ([AMD Athlon X2 7850 Black
    Edition][] and [BIOSTAR TA785 A2+][]) -- \$75.98
-   [Broadway Com Corp R-310][] -- \$19.99
-   [OCZ Value Series 2GB (2 x 1GB) 240-Pin DDR2][] -- \$27.99
-   [OCZ ModXStream Pro OCZ500MXSP 500W][] -- \$29.99

</p>
Bringing the grand total to \$153.95 (after MIRs :-D)

The final piece of the puzzle arrived over a week ago, but couldn't
bring myself to take pacifica down, as everything runs off it. Yesterday
I finally decided to take the plunge. I took the machine down and began
the upgrade process. It took only a few hours to move the hardware
(mobo/cpu/ram/psu/hdd) from the Fractal Design R2 to the R-310 and put
the new hardware into the R2 case (the R-310, by the way, is very
cramped and it took a while to get the motherboard situated, but it
takes up very little space and there's plenty of room and airflow). Then
came the painful process of configuring everything.

For the sake of powersaving I downclock the servers until the CPU
voltage is as low as it can go. The Athlon 2200+ is currently running at
1250 MHz while using a mere 90Watts. I wasn't that lucky with the new
hardware. The Biostar motherboard has options to overvolt the CPU, but
it doesn't allow me to reduce voltage at all. Shame. It took for ever to
figure out how to upgrade the BIOS and how to boot from USB. The manual
is shitty, though if I would have read it carefully I would have saved
myself the time on how to uprade it. After a lot of swearing I managed
to update the BIOS and figured out how to boot from USB. Everything went
better than expected.

Debian decided to be a pain in the ass to install as the netinstall disk
cannot be copied to a flash disk using [UNetbootin][]. Or rather it can
be copied and booted off it, but the installer cannot find the drivers
for the CDROM to copy files and so it fails. Most likely it could be
done, and probably has been done. I found a [site that was promising][],
but the instructions were much longer than what it would take to hook up
a CDROM. The CDROM is still in the case, but I disconnected it to save
power.

The post-install instructions for Debian can be found [here][]. Stay
tuned for more updates on this setup.

  [Fractal Design R2]: http://www.fractal-design.com/?view=product&prod=33
  [slickdeals.net]: http://slickdeals.net
  [newegg.com]: http://newegg.com
  [hardware.reddit]: http://www.reddit.com/r/hardware
  [buildapc.reddit]: http://www.reddit.com/r/buildapc/
  [awesome chart from paulisageek.com]: http://paulisageek.com/compare/cpu/
  [AMD Athlon X2 7850 Black Edition]: http://www.newegg.com/Product/Product.aspx?Item=N82E16819103677
  [BIOSTAR TA785 A2+]: http://www.newegg.com/Product/Product.aspx?Item=N82E16813138282
  [Broadway Com Corp R-310]: http://www.newegg.com/Product/Product.aspx?Item=N82E16811162047
  [OCZ Value Series 2GB (2 x 1GB) 240-Pin DDR2]: http://www.newegg.com/Product/Product.aspx?Item=N82E16820227060
  [OCZ ModXStream Pro OCZ500MXSP 500W]: http://www.newegg.com/Product/Product.aspx?Item=N82E16817341016
  [UNetbootin]: http://unetbootin.sourceforge.net/
  [site that was promising]: http://d-i.pascal.at/
  [here]: http://wiki.alexenko.com/linux:debian:postinstall
