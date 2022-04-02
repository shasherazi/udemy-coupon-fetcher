# Udemy coupon fetcher

Udemy coupon fetcher is a tool that will fetch you 100% off coupons on courses (mostly\*)

## Installation

Clone the git repository by running

```bash
git clone https://github.com/shasherazi/udemy-coupon-fetcher.git
```

After that, `cd` into the git repository by
Clone the git repository by running

```bash
cd udemy-coupon-fetcher
```

Then install the requirements in the `requirements.txt` by

```bash
pip install -r requirements.txt
```

## Usage

Just run the `main.py` file by

```python
python3 main.py
```

It will create a new file `{current date and time}.txt` in the same directory as `main.py` and will start writing the course coupons. You can view the file as the code is running to avoid the wait. It will contain the course names and the coupons in the format

```txt
{courseName}: {couponLink}
```

Enjoy the free courses!
