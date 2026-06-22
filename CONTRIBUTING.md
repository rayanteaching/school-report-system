# قوانین همکاری در پروژه School Report System

این فایل قوانین کار گروهی در پروژه را توضیح می‌دهد. همه اعضای تیم باید قبل از ادامه کار، این قوانین را بخوانند و در کارهای بعدی رعایت کنند.

## ترتیب درست انجام کار

در این پروژه هر کار باید با این ترتیب انجام شود:

```text
Issue
↓
Branch
↓
Code
↓
Test
↓
Commit
↓
Push
↓
Pull Request
↓
Review
↓
Merge
↓
Close Issue
```

## قانون ۱: هیچ‌کس مستقیم روی main کار نمی‌کند

شاخه `main` نسخه اصلی پروژه است. هیچ دانش‌آموزی نباید مستقیم روی `main` کدنویسی کند.

برای هر کار باید یک Branch جدا ساخته شود.

مثال:

```bash
git checkout main
git pull
git checkout -b ui-dashboard
```

## قانون ۲: هر کار باید Issue داشته باشد

در واقع Issue یعنی یک کار مشخص و قابل پیگیری.
قبل از شروع کدنویسی باید مشخص باشد:

* این کار مربوط به کدام Issue است؟
* مسئول این Issue کیست؟
* خروجی مورد انتظار چیست؟
* شرایط پذیرش کار چیست؟

## قانون ۳: هر Pull Request باید به Issue وصل باشد

در توضیح Pull Request باید شماره Issue نوشته شود.

درست:

```text
Related Issue: #21
```

یا اگر قرار است بعد از Merge شدن، Issue بسته شود:

```text
Closes #21
```

نادرست:

```text
Issue مرتبط:
Improve main dashboard layout
```

چون GitHub فقط با شماره Issue می‌تواند ارتباط را تشخیص دهد.

## قانون ۴: عنوان Pull Request باید دقیق باشد

عنوان Pull Request نباید کلی یا نامشخص باشد.

نادرست:

```text
better GUI
```

درست:

```text
Improve main dashboard layout
```

نادرست:

```text
i fix something
```

درست:

```text
Fix student login validation
```

## قانون ۵: توضیح Pull Request باید کامل باشد

هر Pull Request باید این موارد را داشته باشد:

* توضیح کوتاه کار انجام‌شده
* شماره Issue مرتبط
* فایل‌های تغییر کرده
* موارد تغییر یافته
* نتیجه تست

## قانون ۶: قبل از Commit باید برنامه تست شود

هیچ دانش‌آموزی نباید بدون اجرای برنامه Commit بزند.

برای پروژه گرافیکی، حداقل باید بررسی شود:

* پنجره باز می‌شود.
* خطای Python نمایش داده نمی‌شود.
* دکمه‌ها یا فرم‌های مورد نظر دیده می‌شوند.
* برنامه پس از بستن و اجرای دوباره همچنان درست اجرا می‌شود.

## قانون ۷: اگر مربی اصلاح خواست، Pull Request جدید نسازید

اگر مربی زیر Pull Request اصلاح خواست، همان Branch را اصلاح کنید.

مراحل اصلاح:

```bash
git status
git add .
git commit -m "Fix requested changes such as : blah blah blah"
git push
```

بعد از `git push`، همان Pull Request قبلی به‌صورت خودکار به‌روزرسانی می‌شود.

## قانون ۸: Commit message باید واضح باشد

حتما Commit message باید کوتاه، روشن و حرفه‌ای باشد.

نادرست:

```text
i fix idk
```

درست:

```text
Fix dashboard comments
```

نادرست:

```text
better GUI
```

درست:

```text
Improve dashboard visual style
```

## قانون ۹: Merge فقط با تأیید مربی انجام می‌شود

دانش‌آموزان نباید Pull Request خودشان را Merge کنند.

مربی کد را بررسی می‌کند و یکی از این تصمیم‌ها را می‌گیرد:

* تأیید و Merge
* درخواست اصلاح
* بستن Pull Request در صورت مسیر اشتباه

## قانون ۱۰: Issue زمانی بسته می‌شود که کار واقعاً تمام شده باشد

توجه کنید Issue فقط وقتی بسته می‌شود که Pull Request مربوط به آن بررسی و Merge شده باشد.

اگر کار هنوز ناقص است، Issue باید باز بماند.
