# RIG-TARS — richiesta tecnica al produttore (non ancora inviata)

**Destinatario pubblicato dal sito LuwuDynamics:** `hello@xgorobot.com`  
**Fonte contatto:** https://shop.xgorobot.com/policies/privacy-policy  
**Oggetto:** RIG-TARS electronics kit — request for SKU-specific packing list, power specifications and hardware revision  
**Lingua:** inglese (principale) + cinese semplificato (alternativa).  
**Stato:** DRAFT, **non inviato**; nessuna risposta ricevuta.  
**Riferimento interno:** Jira RTARS-9 · https://github.com/pianic2/personal-rig-tars/pull/1

## Messaggio inglese

Hello LuwuDynamics Support,

I purchased your **RIG-TARS Fully Open-Source AI Companion Robot Maker DIY Electronics Kit** from your store:

https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit

I am documenting the actual components and comparing them with your public **RIG-TARS replication BOM V1.0**. I understand that the replication BOM may differ from the **commercial electronics-kit packing list**. Before powering on or assembling the kit, could you please provide the following **for the exact version supplied to me**?

**Kit identification:** PCB marking: `RIG-Board 26/6/2025`; no revision/lot number on the packaging. Three unmarked servos; display flex `FCP-HD240239C12-V1`; camera flex `HBVCAM-2526 V11`.

**1. SKU-specific packing list / hardware revision.** Please provide the expected exact quantities, part numbers and revision for my electronics kit, rather than only the generic replication BOM. Is `RIG-Board 26/6/2025` a PCB design date, and what board revision and wiring diagram correspond to it?

**2. Fasteners: the kit I counted includes:**

| Fastener | Count received |
| --- | ---: |
| M2×6 Phillips self-tapping (bag label) | 55 |
| M2×4 Phillips, round head | 4 |
| M2×4 Phillips, countersunk head | 4 |
| M2×5 Phillips, flat head | 2 |
| M3×8 Phillips, flat head | 1 |
| M2 hex lock nut (bag label) | 1 |
| M2×4 hex-socket screws with pre-applied threadlocker | 0 |
| M2×10 hex locking screw sets | 0 |
| M3×10 Phillips screws | 0 |
| M3 self-locking nuts | 0 |
| Electronics insulating foam | 0 |

Your replication BOM lists 60 M2×6 screws (with “52” in its description), plus different M2×4 hex-socket, M2×10 hex locking group, M3×10, M3 nuts and foam. **Are the components I received correct for the revised commercial kit?** Which fastener should be used at each servo, connecting link, USB-C mounting point and hardware-platform fixation? Please attach the fastener table or assembly drawing corresponding to the shipped kit. I will not substitute different screw dimensions without confirmation.

**3. Battery: safety-critical.** The included blue battery pack has **no printed specifications**. New close-up PCB photographs show a 2-pin socket with marked `+` on the left and `−` on the right (components-facing view, servo headers top, USB-C bottom right), and an IC marked `SLM6800` near the battery socket. The SLM6800 vendor describes it as a two-cell Li-ion charger; **this does not establish the shipped pack specification or its plug wiring**. Please confirm for this *exact pack and PCB*: manufacturer/part number, cell chemistry, nominal and maximum charging voltage, capacity (mAh), number of cells, protection/BMS, charge procedure, allowed charger/USB charging behavior, connector model, pin order and polarity (with a clear drawing). I will not connect or charge it until identified.

**4. Display controller.** Your replication BOM says `ST7789P3`, while the current RIG-Omni TARS documentation says `ST7789V2 320×240`. The supplied flex marking is `FCP-HD240239C12-V1`. Which controller and firmware/display initialization are correct for the supplied display?

**5. Servos and board.** Are the 3 unmarked servos `SCS009` (including model/revision `SCS009-20201118-D`), and what are the correct bus voltage, servo IDs/protocol, and wiring for the supplied board? Is there a TARS-specific schematic or board pinout corresponding to `RIG-Board 26/6/2025`?

**6. Foam/insulation.** Is the insulating foam listed in the replication BOM a required safety/installation part for this commercial kit, and if so, what material/thickness and location are specified?

Could you please share **the exact assembly video/manual revision, electronics wiring diagram, and packing list** matching the hardware shipped to me? The public diagrams for other RIG models should not be assumed interchangeable.

I can provide clear photographs of the board, all fastener bags, battery and display if needed.

Thank you.

---

## 简体中文（供陆吾技术支持参考）

**主题：RIG-TARS 电子套件——请求确认实际装箱清单、主板版本、电池规格与螺丝规格**

陆吾智能技术支持团队，您好！

我购买了贵司的 **RIG-TARS 电子 DIY 套件**：  
https://shop.xgorobot.com/products/rig-tars-fully-open-source-3d-printed-programmable-ai-companion-robot-maker-diy-kit

我正在整理实物物料清单，并与官网公布的 **RIG-TARS 复刻 BOM V1.0** 对照。我理解复刻用 BOM 可能与实际销售的电子套件装箱清单不同。为了安全组装和上电，请帮忙确认**我收到的这个版本**的准确资料。

**硬件标识：** 主板丝印 `RIG-Board 26/6/2025`；包装没有版本号或批次号。三台舵机没有型号标签；屏幕排线标识为 `FCP-HD240239C12-V1`，摄像头排线为 `HBVCAM-2526 V11`。

**1．装箱清单和主板版本。** 请提供对应本次销售套件的完整装箱清单（各零件型号、数量、硬件版本），而不仅是通用的复刻 BOM。主板上的 `26/6/2025` 是否是设计日期？这块主板对应哪个版本的接线图和原理图？

**2．螺丝和螺母核对。** 我实际清点的数量如下：

| 类型 | 实际数量 |
| --- | ---: |
| M2×6 十字自攻螺丝（按袋上标识） | 55 |
| M2×4 圆头十字螺丝 | 4 |
| M2×4 沉头十字螺丝 | 4 |
| M2×5 平头十字螺丝 | 2 |
| M3×8 平头十字螺丝 | 1 |
| M2 六角对锁螺母（按袋上标识） | 1 |
| M2×4 内六角杯头点胶螺丝 | 0 |
| M2×10 六角对锁螺丝组 | 0 |
| M3×10 十字螺丝 | 0 |
| M3 防松螺母 | 0 |
| 电子绝缘泡棉 | 0 |

公开的复刻 BOM 写的是 M2×6 螺丝 60 枚（名称中又出现 52 枚），并列出了其他规格的内六角螺丝、M2×10 螺丝组、M3×10 螺丝、M3 螺母和绝缘泡棉。请确认：**我收到的配件是否符合当前销售版本的要求？** 舵机、连杆、Type-C 接口和主板安装位置分别应使用哪种螺丝？请提供对应实际发货版本的螺丝规格表或装配图。在确认前我不会擅自替换螺丝。

**3．电池规格（安全重点）。** 套件附带的蓝色电池包没有任何印刷规格。新照片显示主板二针电池座旁标有 `+` 和 `−`（正面朝上、舵机插座在上、USB-C 在右下时：左正右负）；附近芯片标有 `SLM6800`，厂家将其描述为双节锂电池充电 IC。**这不能证明收到的电池包电压、化学体系或插头实际线序**。请明确告知此电池包的型号、化学体系、额定电压、最高充电电压、容量（mAh）、电芯数量、保护板/BMS、正确充电方法、是否支持通过主板 USB 充电，以及插头型号、引脚顺序和正负极（最好附接线图）。在确认这些信息之前，我不会连接或充电。

**4．屏幕驱动。** 复刻 BOM 写的是 `ST7789P3`，而目前 RIG-Omni 的 TARS 文档写的是 `ST7789V2 320×240`。我收到的屏幕排线标识为 `FCP-HD240239C12-V1`。请确认它实际使用哪种驱动芯片，以及适配的固件显示配置。

**5．舵机和主板。** 三台无标签舵机是否为 `SCS009`（或 `SCS009-20201118-D`）？请提供其供电电压、总线协议、默认 ID、接线方式，以及 `RIG-Board 26/6/2025` 对应的 TARS 专用原理图或接口定义。

**6．绝缘泡棉。** 复刻 BOM 中的电子绝缘泡棉，是否为这个销售套件必须使用的部件？若需要，请提供材质、厚度及准确安装位置。

烦请发送**与我收到的硬件版本一致**的装配说明、接线图和装箱清单。我可以按需提供主板、电池、屏幕和螺丝包的清晰照片。

谢谢！

---

## Quando arriverà la risposta

1. Conservare la risposta originale (messaggio, eventuali allegati e data) con riferimento Jira RTARS-9.
2. Per ogni risposta associare i riferimenti `D01,D02,D04,D05,D06,D07,D08,D09,D13` e distinguere `verified` da `requires measurement`.
3. NON equiparare una dichiarazione generica su RIG-Puppy/Hover/Arm alla versione TARS, in particolare per batteria e schema elettrico.
4. La chiusura dei gap di montaggio deve precedere l'avvio dell'assemblaggio e della prima accensione.

## Foto PCB successivamente ricevute

Prima di inviare questo messaggio, il proprietario ha fornito foto ravvicinate dei due lati PCB. I nuovi dati non erano presenti nella richiesta originale: `RIG-Board 26/6/25`, modulo ESP32-S3-WROOM-1 / MCN16R8, chip SLM6800 e polarità della **presa sulla board** (+ sinistra / − destra nell'orientamento descritto). Non chiedere di nuovo al fornitore la semplice serigrafia, bensì **identità del pacco e compatibilità 2S, cablaggio del plug rispetto all'orientamento della presa, BMS, soglie carica, revisione della board, schema della carrier**. Rimane **draft non inviato**.
