import React from 'react';
import { render } from '@testing-library/react';
import {IconsAdapter} from "."

test('Рендеринг IconsAdapter компонента', () => {
    const {container} = render(<IconsAdapter iconType={"Icon28LikeOutline"} />);
    expect(container).toMatchSnapshot()
})