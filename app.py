import streamlit as st
landing_page_cn = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="description" content="重庆国际医美中心，提供胸部美学塑形与轻奢休养旅行一站式服务。JCI认证机构，持证医师团队，严格隐私保护。">
<meta name="theme-color" content="#0f172a">
<title>重庆医美轻奢之旅 | 胸部美学塑形 · 五星休养 · 一站式海外医疗</title>

<!-- Preconnect -->
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>

<!-- Critical CSS inlined -->
<style>
/* Reset & Base */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Segoe UI",Roboto,sans-serif;line-height:1.7;color:#334155;background:#fff;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{text-decoration:none;color:inherit}
button{border:none;background:none;cursor:pointer;font-family:inherit}

/* Design Tokens */
:root{
  --primary:#0f172a;
  --accent:#c9a96e;
  --accent-dark:#a88b55;
  --text:#334155;
  --text-light:#64748b;
  --bg:#f8fafc;
  --white:#ffffff;
  --success:#059669;
  --border:#e2e8f0;
  --shadow:0 4px 6px -1px rgba(0,0,0,0.05),0 2px 4px -2px rgba(0,0,0,0.05);
  --shadow-lg:0 10px 15px -3px rgba(0,0,0,0.08),0 4px 6px -4px rgba(0,0,0,0.08);
}

/* Utility */
.container{width:100%;max-width:480px;margin:0 auto;padding:0 20px}
.text-center{text-align:center}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}

/* Buttons */
.btn-wa{
  display:inline-flex;align-items:center;justify-content:center;gap:8px;
  background:linear-gradient(135deg,#25d366 0%,#128c7e 100%);
  color:#fff;font-weight:600;font-size:16px;padding:16px 32px;
  border-radius:50px;width:100%;box-shadow:0 4px 12px rgba(37,211,102,0.3);
  transition:transform .15s,box-shadow .15s;position:relative;overflow:hidden
}
.btn-wa:active{transform:scale(.98)}
.btn-wa svg{width:22px;height:22px;flex-shrink:0}

/* Floating CTA */
.float-cta{
  position:fixed;bottom:0;left:0;right:0;z-index:100;
  background:rgba(255,255,255,0.95);backdrop-filter:blur(10px);
  border-top:1px solid var(--border);padding:12px 20px;
  box-shadow:0 -4px 20px rgba(0,0,0,0.08);
}
.float-cta .container{max-width:480px;padding:0 16px}
.float-cta .btn-wa{padding:14px 24px;font-size:15px}

/* Header/Hero */
.hero{
  background:linear-gradient(180deg,#0f172a 0%,#1e293b 100%);
  color:#fff;padding:80px 20px 100px;position:relative;overflow:hidden
}
.hero::before{
  content:"";position:absolute;top:-50%;right:-20%;width:300px;height:300px;
  background:radial-gradient(circle,rgba(201,169,110,0.15) 0%,transparent 70%);
  border-radius:50%;pointer-events:none
}
.hero-badge{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(201,169,110,0.15);border:1px solid rgba(201,169,110,0.3);
  color:var(--accent);font-size:11px;font-weight:600;letter-spacing:0.05em;
  text-transform:uppercase;padding:6px 14px;border-radius:100px;margin-bottom:20px
}
.hero h1{font-size:28px;font-weight:700;line-height:1.35;margin-bottom:16px;letter-spacing:-0.01em}
.hero h1 span{color:var(--accent)}
.hero-sub{font-size:16px;color:#94a3b8;line-height:1.7;margin-bottom:32px;max-width:400px}
.hero-trust{display:flex;gap:20px;margin-top:28px;font-size:12px;color:#64748b}
.hero-trust-item{display:flex;align-items:center;gap:6px}
.hero-trust-item svg{width:16px;height:16px;color:var(--accent)}

/* Sections */
.section{padding:56px 0}
.section-title{font-size:22px;font-weight:700;color:var(--primary);margin-bottom:12px;line-height:1.3}
.section-sub{font-size:14px;color:var(--text-light);margin-bottom:32px}

/* Brand Intro */
.brand-intro{background:var(--bg)}
.brand-card{
  background:var(--white);border-radius:16px;padding:24px;
  box-shadow:var(--shadow);border:1px solid var(--border)
}
.brand-card p{font-size:14px;color:var(--text);margin-bottom:12px}
.brand-card p:last-child{margin-bottom:0}
.brand-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px}
.stat-item{text-align:center}
.stat-num{display:block;font-size:24px;font-weight:700;color:var(--accent);line-height:1}
.stat-label{font-size:11px;color:var(--text-light);margin-top:4px;text-transform:uppercase;letter-spacing:0.05em}

/* Services */
.service-list{display:grid;gap:16px}
.service-card{
  background:var(--white);border-radius:12px;padding:20px;
  border:1px solid var(--border);display:flex;gap:16px;align-items:flex-start
}
.service-icon{
  width:48px;height:48px;border-radius:12px;
  background:linear-gradient(135deg,#f8fafc 0%,#e2e8f0 100%);
  display:flex;align-items:center;justify-content:center;flex-shrink:0
}
.service-icon svg{width:24px;height:24px;color:var(--accent)}
.service-content h3{font-size:16px;font-weight:600;color:var(--primary);margin-bottom:6px}
.service-content p{font-size:13px;color:var(--text-light);line-height:1.6}

/* Travel */
.travel-section{background:var(--primary);color:#fff}
.travel-section .section-title{color:#fff}
.travel-section .section-sub{color:#94a3b8}
.travel-grid{display:grid;gap:16px}
.travel-card{
  background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
  border-radius:12px;padding:20px
}
.travel-card h3{font-size:16px;font-weight:600;margin-bottom:8px;color:#f1f5f9}
.travel-card p{font-size:13px;color:#94a3b8;line-height:1.7}

/* Why Choose */
.why-grid{display:grid;gap:20px}
.why-item{display:flex;gap:14px;align-items:flex-start}
.why-num{
  width:36px;height:36px;border-radius:50%;background:var(--bg);
  color:var(--accent);font-weight:700;font-size:14px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0
}
.why-content h4{font-size:15px;font-weight:600;color:var(--primary);margin-bottom:4px}
.why-content p{font-size:13px;color:var(--text-light);line-height:1.6}

/* Process */
.process-section{background:var(--bg)}
.process-steps{position:relative;padding-left:28px}
.process-steps::before{
  content:"";position:absolute;left:11px;top:8px;bottom:32px;
  width:2px;background:linear-gradient(180deg,var(--accent) 0%,var(--border) 100%)
}
.step{position:relative;margin-bottom:32px}
.step:last-child{margin-bottom:0}
.step-dot{
  position:absolute;left:-28px;top:2px;width:24px;height:24px;
  background:var(--white);border:2px solid var(--accent);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:700;color:var(--accent)
}
.step h4{font-size:16px;font-weight:600;color:var(--primary);margin-bottom:6px}
.step p{font-size:13px;color:var(--text-light);line-height:1.7}

/* Booking */
.booking-section{text-align:center;padding-bottom:100px}
.booking-box{
  background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);
  border-radius:20px;padding:40px 24px;color:#fff;position:relative;overflow:hidden
}
.booking-box::before{
  content:"";position:absolute;top:-30%;left:-20%;width:200px;height:200px;
  background:radial-gradient(circle,rgba(201,169,110,0.2) 0%,transparent 70%);
  border-radius:50%
}
.booking-box h2{font-size:22px;font-weight:700;margin-bottom:12px;position:relative}
.booking-box p{font-size:14px;color:#94a3b8;margin-bottom:24px;position:relative;max-width:320px;margin-left:auto;margin-right:auto}
.booking-box .btn-wa{position:relative;max-width:280px;margin:0 auto}

/* Footer */
.footer{
  background:#0f172a;color:#64748b;font-size:11px;padding:40px 20px 120px;
  border-top:1px solid #1e293b
}
.footer-grid{display:grid;gap:24px;margin-bottom:24px}
.footer-block h4{font-size:12px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:10px}
.footer-block p,.footer-block a{font-size:11px;line-height:1.9;color:#64748b;display:block}
.footer-block a:hover{color:#94a3b8}
.footer-divider{height:1px;background:#1e293b;margin:24px 0}
.footer-bottom{text-align:center}
.footer-bottom p{margin-bottom:4px}

/* Reduced motion */
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .btn-wa{transition:none}
}

/* Small height devices */
@media (max-height:700px){
  .hero{padding:60px 20px 80px}
  .section{padding:40px 0}
}
</style>
</head>

<body>

<!-- Hero Section -->
<section class="hero" id="top">
  <div class="container">
    <div class="hero-badge">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      海外医疗旅游 · 仅限18岁以上
    </div>
    <h1>重庆胸部美学塑形 <span>+</span> 轻奢休养之旅</h1>
    <p class="hero-sub">持证医师团队 · JCI认证机构 · 严格隐私保护<br>将专业医疗与山城休养结合，为东南亚华人提供一站式安心之选</p>
    <a href="https://wa.me/861234567890?text=您好，我想了解重庆胸部美学塑形及休养旅行套餐的详细信息，请发送资料。" class="btn-wa" target="_blank" rel="noopener noreferrer">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.89c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
      WhatsApp 立即咨询
    </a>
    <div class="hero-trust">
      <div class="hero-trust-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        JCI国际认证
      </div>
      <div class="hero-trust-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7h-9"/><path d="M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg>
        仅限18岁以上
      </div>
      <div class="hero-trust-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
        严格隐私保护
      </div>
    </div>
  </div>
</section>

<!-- Brand Intro -->
<section class="section brand-intro" id="about">
  <div class="container">
    <h2 class="section-title text-center">专业医疗 · 安心之选</h2>
    <p class="section-sub text-center">立足重庆国际医疗中心，服务东南亚华人社群，以透明、严谨、尊重为基石</p>
    <div class="brand-card">
      <p>我们依托重庆首家通过JCI国际认证的医疗中心开展服务，整形外科团队均持有中国卫生部颁发的《医师执业证书》及《医疗美容主诊医师资格证》。从初诊评估到术后随访，每一步均有标准化医疗流程保障。</p>
      <p>我们坚持「知情同意」原则：术前提供详尽的方案说明与风险告知，不夸大效果，不隐瞒风险，让每一位客人在充分了解的基础上做出自主决定。</p>
      <div class="brand-stats">
        <div class="stat-item">
          <span class="stat-num">12+</span>
          <span class="stat-label">年行业深耕</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">JCI</span>
          <span class="stat-label">国际认证</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">多语种</span>
          <span class="stat-label">服务团队</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Services -->
<section class="section" id="services">
  <div class="container">
    <h2 class="section-title text-center">胸部美学塑形服务</h2>
    <p class="section-sub text-center">根据个体解剖条件与期望，提供个性化医疗方案。效果因人而异，需经专业评估。</p>
    <div class="service-list">
      <div class="service-card">
        <div class="service-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 7.8l-7.7 7.7-4-4-5.7 5.7"/><path d="M15 7h6v6"/></svg>
        </div>
        <div class="service-content">
          <h3>假体植入塑形</h3>
          <p>采用经中国NMPA及国际认证的假体材料，根据胸廓宽度、皮肤张力等个体条件，选择合适形态与植入层次。手术在层流净化手术室完成，配备专业麻醉团队全程监护。</p>
        </div>
      </div>
      <div class="service-card">
        <div class="service-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 11-11.31 0z"/></svg>
        </div>
        <div class="service-content">
          <h3>自体脂肪移植</h3>
          <p>抽取腰腹或大腿多余脂肪，经纯化处理后移植至胸部。适合追求自然触感、同时希望改善身体曲线的客人。脂肪存活率存在个体差异，可能需要二次调整。</p>
        </div>
      </div>
      <div class="service-card">
        <div class="service-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 00-2.91-.09z"/><path d="M12.5 15.5l-2-2"/><path d="M20 2l2 2-7.5 7.5-2-2L20 2z"/></svg>
        </div>
        <div class="service-content">
          <h3>修复与调整</h3>
          <p>针对假体置换、包膜挛缩、形态不对称等情况提供修复评估。医师将根据既往手术记录与当前组织状态，制定务实、可操作的改善方案。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Travel -->
<section class="section travel-section" id="travel">
  <div class="container">
    <h2 class="section-title text-center">重庆轻奢休养之旅</h2>
    <p class="section-sub text-center">术后恢复期间，在安全与舒适的前提下，感受山城的独特魅力</p>
    <div class="travel-grid">
      <div class="travel-card">
        <h3>五星休养套房</h3>
        <p>入住合作五星级酒店休养楼层，配备术后护理包、营养膳食及24小时中文/英文/马来语管家服务。每日医护巡房，确保恢复进程受控。</p>
      </div>
      <div class="travel-card">
        <h3>山城文化轻体验</h3>
        <p>恢复后期，在医师许可下安排轻度活动：长江索道观景、洪崖洞夜景漫步、地道火锅私宴（忌口期提供定制营养餐）。全程专车接送，避免劳累。</p>
      </div>
      <div class="travel-card">
        <h3>一站式行程管家</h3>
        <p>提供签证协助、机场VIP接机、本地电话卡、医疗翻译陪同。所有医疗预约与休闲行程由专属管家协调，您只需专注休养。</p>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose -->
<section class="section" id="why">
  <div class="container">
    <h2 class="section-title text-center">为何选择我们</h2>
    <p class="section-sub text-center">透明、安全、尊重隐私 —— 海外医疗的核心底线</p>
    <div class="why-grid">
      <div class="why-item">
        <div class="why-num">1</div>
        <div class="why-content">
          <h4>持证医师主刀</h4>
          <p>主刀医师均具备整形外科副主任医师以上职称，持有国家卫健委颁发的医疗美容主诊资格。手术方案经多学科团队讨论，而非单人决策。</p>
        </div>
      </div>
      <div class="why-item">
        <div class="why-num">2</div>
        <div class="why-content">
          <h4>JCI认证医疗环境</h4>
          <p>手术室空气洁净度达万级标准，配备进口麻醉机与生命监护系统。术后恢复区独立设置，与普通病区完全隔离，降低感染风险。</p>
        </div>
      </div>
      <div class="why-item">
        <div class="why-num">3</div>
        <div class="why-content">
          <h4>绝对隐私保护</h4>
          <p>独立电梯、私密通道、加密病历系统。未经本人书面授权，任何信息不向第三方披露，包括家属。符合国际患者数据保护标准。</p>
        </div>
      </div>
      <div class="why-item">
        <div class="why-num">4</div>
        <div class="why-content">
          <h4>术后远程随访</h4>
          <p>离院后提供6个月免费远程随访服务，通过WhatsApp视频或图文方式与主刀医师保持联系，及时解答恢复期的任何疑问。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Process -->
<section class="section process-section" id="process">
  <div class="container">
    <h2 class="section-title text-center">四步安心流程</h2>
    <p class="section-sub text-center">为海外客人量身定制的全周期服务</p>
    <div class="process-steps">
      <div class="step">
        <div class="step-dot">1</div>
        <h4>远程视频初诊</h4>
        <p>通过加密视频与主刀医师一对一沟通，提交既往病史与近期体检报告。医师初步评估手术可行性，如实告知预期效果与潜在风险。无任何前期费用。</p>
      </div>
      <div class="step">
        <div class="step-dot">2</div>
        <h4>定制方案与行程</h4>
        <p>确认手术意向后，收到包含手术方案、费用明细、行程安排的正式文件。我们协助办理医疗签证所需邀请函，并预订休养酒店。</p>
      </div>
      <div class="step">
        <div class="step-dot">3</div>
        <h4>抵渝手术与监护</h4>
        <p>抵达当日完成术前体检复核。手术由主刀医师与麻醉团队共同执行，术后24小时入住ICU观察区，之后转入休养套房。</p>
      </div>
      <div class="step">
        <div class="step-dot">4</div>
        <h4>休养复查与返程</h4>
        <p>术后第3天、第7天安排门诊复查，确认恢复良好后安排返程。离院时携带完整中英文病历、术后护理指南及医师紧急联系方式。</p>
      </div>
    </div>
  </div>
</section>

<!-- Booking -->
<section class="section booking-section" id="contact">
  <div class="container">
    <div class="booking-box">
      <h2>开启您的专属咨询</h2>
      <p>添加我们的WhatsApp，直接与中文医疗顾问沟通。获取手术资料包、医师资质文件及参考行程方案。</p>
      <a href="https://wa.me/861234567890?text=您好，我想了解重庆胸部美学塑形及休养旅行套餐的详细信息，请发送资料。" class="btn-wa" target="_blank" rel="noopener noreferrer">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.89c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
        WhatsApp 立即咨询
      </a>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer" id="legal">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-block">
        <h4>隐私政策</h4>
        <p>我们仅收集用于医疗评估与行程安排的必要个人信息。所有数据采用加密存储，未经您书面授权绝不向任何第三方披露。您有权随时要求删除个人数据。</p>
      </div>
      <div class="footer-block">
        <h4>服务条款</h4>
        <p>本网站仅提供信息服务，不构成医患关系确立。所有服务需经现场医疗评估后方可确认。页面所示价格为参考区间，最终费用以实际方案为准。我们不提供急诊医疗服务。</p>
      </div>
      <div class="footer-block">
        <h4>医疗免责声明</h4>
        <p>医疗美容效果受个体体质、术后护理、恢复能力等多种因素影响，存在显著个体差异。我们无法保证任何特定美学结果。所有手术均存在固有风险，包括但不限于感染、出血、疤痕、麻醉反应等，医师将在术前详细说明。本服务仅限年满18周岁且身体健康的成年人。</p>
      </div>
    </div>
    <div class="footer-divider"></div>
    <div class="footer-bottom">
      <p>重庆国际医美与 wellness 中心</p>
      <p>持有《医疗机构执业许可证》| JCI国际认证成员</p>
      <p style="margin-top:8px;color:#475569">本服务仅限18周岁及以上成年人咨询与预约</p>
    </div>
  </div>
</footer>

<!-- Floating CTA -->
<div class="float-cta">
  <div class="container">
    <a href="https://wa.me/861234567890?text=您好，我想了解重庆胸部美学塑形及休养旅行套餐的详细信息，请发送资料。" class="btn-wa" target="_blank" rel="noopener noreferrer">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.89c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
      WhatsApp 立即咨询
    </a>
  </div>
</div>

<!-- Minimal JS -->
<script>
(function(){
  // Lazy load images
  var imgs=document.querySelectorAll('img[data-src]');
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          var img=entry.target;
          img.src=img.dataset.src;
          img.onload=function(){img.classList.add('loaded')};
          obs.unobserve(img);
        }
      });
    },{rootMargin:'50px'});
    imgs.forEach(function(img){obs.observe(img)});
  }else{
    imgs.forEach(function(img){img.src=img.dataset.src;img.classList.add('loaded')});
  }
  
  // Anchor offset for floating bar
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=this.getAttribute('href');
      if(id==='#')return;
      var el=document.querySelector(id);
      if(el){
        e.preventDefault();
        var y=el.getBoundingClientRect().top+window.pageYOffset-80;
        window.scrollTo({top:y,behavior:'smooth'});
      }
    });
  });
})();
</script>
